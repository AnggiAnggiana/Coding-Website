from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Course
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from django.urls import reverse
from django.contrib import messages
from .models import Student
from .models import Profile
from .models import Class
from .forms import ClassForm
from .forms import CourseForm
from django.http import HttpResponse
import csv

# Import form untuk payment
from .models import Payment

# Dibawah ini untuk download pdf
# Masukan di terminal: pip install reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# import forms payment kelas yg dipilih
from .forms import PaymentForm

# Dibawah ini untuk pagniation(penomoran halaman/page website)
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404


# User = get_user_model()

def homepage(request, month=datetime.now().strftime('%B'), year=datetime.now().year):
    nama = "Anggi"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # Waktu Hari ini/sekarang
    now = datetime.now()
    current_month = now.strftime('%B')
    current_year = now.year
    time = now.strftime('%H:%M %p')

    # Make calendar
    kalender = HTMLCalendar().formatmonth(
        year,
        month_number
        )
    return render(request, 'kelas_programming/homepage.html', {
        "namaku": nama,
        "month": month,
        "year": year,
        "current_month": current_month,
        "current_year": current_year,
        "time": time,
        "month_number": month_number,
        "kalender" : kalender,
    })

@login_required()
def list_kelas(request):
    list_kelas_coding = Course.objects.all()
    return render(request, 'kelas_programming/course.html', {
        'list_kelas_coding': list_kelas_coding,
    })


# Membuat page form untuk membuat course baru
@login_required
def add_course(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            # Versi 1 (awal tanpa "owner" di models.py)
            form.save()
            messages.success(request, 'Course berhasil ditambahkan')
            return redirect(reverse('list_kelas') + '?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'kelas_programming/add_course.html', {
        'form' : form,
        'submitted': submitted
    })


# Membuat page untuk mengedit course
@login_required
def edit_course(request, course_id):
    edit_course = Course.objects.get(pk=course_id)
    form = CourseForm(request.POST or None, instance=edit_course)
    if form.is_valid():
        form.save()
        messages.success(request, 'Berhasil mengedit course!!')
        return redirect('list_kelas')
    
    return render(request, 'kelas_programming/edit_course.html',
                {
                    'edit_course': edit_course,
                    'form': form
                })


# Menghapus course
@login_required
def delete_course(request, course_id):
    delete_course = Course.objects.get(pk=course_id)
    course_name = str(delete_course)
    delete_course.delete()
    messages.success(request, f"Berhasil menghapus course '{course_name}'")
    return redirect('list_kelas')

# Membuat page untuk tombol "lihat" pada page course
# Masukan owner seperti pada "edit_profile" untuk membuat kelas bisa dipilih berdasarkan ownernya
@login_required
def view_kelas(request, kelas_id):
    view_kelas = Class.objects.get(pk=kelas_id)
    return render(request, 'kelas_programming/show_kelas.html',{
        'view_kelas': view_kelas})
    

# Membuat page untuk content myclass
@login_required
def class_content(request, kelas_id):
    student = Payment.objects.filter(siswa__owner=request.user.id)
    profile = Student.objects.filter(owner=request.user.id)
    class_content = Class.objects.get(pk=kelas_id)
    return render(request, 'kelas_programming/class_content.html', {
        'student': student,
        'profile': profile,
        'class_content': class_content,
    })
    
# INI DATA "LOGIN WITH GOOGLE"
# CLIENT ID: 511071097404-8kmoiupe2osf4rae7b34ft4oiel19lds.apps.googleusercontent.com
# CLIENT SECRET: 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

    

# Page untuk pembayaran sebelum memilih kelas
@login_required
def paymentKelas(request, kelas_id):
    submitted = False
    pembayaran = Class.objects.get(pk=kelas_id)
    if request.method == "POST":
        form = PaymentForm(request.POST, user=request.user, kelas_id=kelas_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sekarang kamu bisa mengakses kelas')
            return redirect(reverse('myclass') + '?submitted=True')
    else:
        form = PaymentForm(user=request.user, kelas_id=kelas_id)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'kelas_programming/payment.html', {
        'pembayaran': pembayaran,
        'form' : form,
        'submitted': submitted
    })


# Membuat page untuk tombol "masuk kelas" 
@login_required
def myclass(request):
    student = Payment.objects.filter(siswa__owner=request.user.id)
    profile = Student.objects.filter(owner=request.user.id)
    return render(request, 'kelas_programming/myclass.html', {
        'student': student,
        'profile': profile
    })

# Menambahkan pagination di def kelas ini
@login_required 
def kelas(request):
    kelas = Class.objects.all()

    # Menambahkan pagination/penomoran page website
    # Angka 2 dalam kurung dibawah menunjukkan jumlah kelas yg bisa dilihhat dalam 1 page
    pagin = Paginator(Class.objects.all(), 3)
    page = request.GET.get('page')
    classes = pagin.get_page(page)
    # Kode pageAngka dibawah ini untuk membuat pagination/penomoran halaman bisa di klik
    # pageAngka = "1" * classes.paginator.num_pages
    pageAngka = range(1, classes.paginator.num_pages +1)

    return render(request, 'kelas_programming/class.html', {
        'kelas': kelas,
        'classes': classes,
        'pageAngka': pageAngka})



# Membuat page yg muncul hanya berdasarkan id kelas tertentu
# @login_required
# def show_kelas(request, kelas_id):
#     show_kelas = Class.objects.get(pk=kelas_id)
#     return render(request, 'kelas_programming/show_kelas.html', {'show_kelas': show_kelas})


@login_required
def edit_kelas(request, kelas_id):
    edit_kelas = Class.objects.get(pk=kelas_id)
    form = ClassForm(request.POST or None, instance=edit_kelas)
    if form.is_valid():
        form.save()
        return redirect('kelas')
    
    return render(request, 'kelas_programming/edit_kelas.html',
                {
                    'edit_kelas': edit_kelas,
                    'form': form
                })

# Membuat search bar untuk mencari kelas
@login_required
def search_kelas(request):
    if request.method == "POST":
        mencari = request.POST['mencari']
        # Link ke spesifik kelas
        # kelas = Class.objects.all()
        kelas = Class.objects.filter(framework__icontains=mencari)
        kelas1 = Class.objects.filter(language__icontains=mencari)
        kelas2 = Class.objects.filter(function__icontains=mencari)
        kelas3 = Course.objects.filter(lecture__icontains=mencari)
        return render(request, 'kelas_programming/search_kelas.html', {'mencari': mencari, 'kelas': kelas, 'kelas1': kelas1, 'kelas2': kelas2, 'kelas3': kelas3})
    else:
        return render(request, 'kelas_programming/search_kelas', {})
    

@login_required
def myprofile(request):
    # Semua data
    # profile = Student.objects.all()

    # Hanya profile user tertentu
    profile = Student.objects.filter(owner=request.user.id)
    return render(request, 'kelas_programming/myprofile.html', {
        'profile': profile
    })

@login_required
def edit_profile(request):
    submitted = False
    profile_edit = get_object_or_404(Student, owner=request.user.id)
    if request.method == 'POST':
        form = StudentForm(request.POST or None, request.FILES or None, instance=profile_edit)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.owner = request.user.id
            edit_profile.save()
            messages.success(request, 'Profile berhasil diupdate')
            return redirect(reverse('myprofile') + '?submitted=True')

    else:
        form = StudentForm(instance=profile_edit)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'kelas_programming/edit_profile.html', {
        'form': form,
        'submitted': submitted
    })



# Mendownload file CSV Class/Kelas dari website
# Buka website: reportlab.com\docs/reportlab-userguide.pdf
@login_required
def download_class_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=class.csv'

    # Mencantumkan penulis filenya
    writer = csv.writer(response)

    # Isi filenya apa saja
    classes = Class.objects.all()

    # Membuat kolom yg akan dibuat dalam file CSV
    writer.writerow(['Class Name', 'Language', 'Framework', 'Function', 'Link'])

    # Membuat output di filenya
    for kelas in classes:
        writer.writerow([kelas.name, kelas.language, kelas.framework, kelas.function, kelas.link])
    
    return response


# Mendownload file pdf Class/Kelas dari website
# Step 1 ketik di terminal: pip install reportlab
# Step 2 ikutin def dibawah ini
@login_required
def download_class_pdf(request):
    # Membuat Bytestream buffer
    buf = io.BytesIO()

    # membuat canvas/blank page
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    # Membuat teks objectnya
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont("Helvetica", 12)

    # Isi filenya apa saja
    classes = Class.objects.all()

    # Membuat baris teks
    lines = []

    for kelas in classes:
        lines.append(kelas.name)
        lines.append(kelas.language)
        lines.append(kelas.framework)
        lines.append(kelas.function)
        lines.append(kelas.link)
        lines.append("---------------------------------------------")

    # Looping
    for baris in lines:
        textobject.textLine(baris)

    # Mengeksekusi jadi file
    c.drawText(textobject)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='class.pdf')





# def change_password(request):
#     if request.method == 'POST':
#         form = Change_PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Password Berhasil Dirubah')
#             return redirect(reverse('login'))
#         else:
#             messages.success(request, 'Password gagal dirubah')
#             return redirect(reverse('change_password'))
#     else:
#         form = Change_PasswordForm()
#     return render(request, 'kelas_programming/change_password.html', {'form': form})

