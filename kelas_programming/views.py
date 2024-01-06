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

# Import form for payment
from .models import Payment

# These are for download file in pdf
# Type in terminal: pip install reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# import forms payment
from .forms import PaymentForm

from django.shortcuts import get_object_or_404



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


# Page to create new course
@login_required
def add_course(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
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


# Page to edit course
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


# Delete course
@login_required
def delete_course(request, course_id):
    delete_course = Course.objects.get(pk=course_id)
    course_name = str(delete_course)
    delete_course.delete()
    messages.success(request, f"Berhasil menghapus course '{course_name}'")
    return redirect('list_kelas')

# Page for the class in the course
@login_required
def view_kelas(request, kelas_id):
    view_kelas = Class.objects.get(pk=kelas_id)
    return render(request, 'kelas_programming/show_kelas.html',{
        'view_kelas': view_kelas})
    

# Page for payment form
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


# Page to show the choosen class from payment form, named "myclass"
@login_required
def myclass(request):
    student = Payment.objects.filter(siswa__owner=request.user.id)
    profile = Student.objects.filter(owner=request.user.id)
    return render(request, 'kelas_programming/myclass.html', {
        'student': student,
        'profile': profile
    })
    
# Page to show the content in "myclass"
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
    
    
# For the search bar
@login_required
def search_kelas(request):
    if request.method == "POST":
        mencari = request.POST['mencari']
        course = Course.objects.filter(name__icontains=mencari)
        course1 = Class.objects.filter(name__icontains=mencari)
        course2 = Course.objects.filter(lecture__icontains=mencari)
        return render(request, 'kelas_programming/search_kelas.html', {'mencari': mencari, 'course': course, 'course1': course1, 'course2': course2})
    else:
        return render(request, 'kelas_programming/search_kelas', {})
    

# Page for my profile(user profile)
@login_required
def myprofile(request):
    # Hanya profile user tertentu
    profile = Student.objects.filter(owner=request.user.id)
    return render(request, 'kelas_programming/myprofile.html', {
        'profile': profile
    })

# Page for edit profile
@login_required
def edit_profile(request):
    submitted = False
    profile_edit, created = Student.objects.get_or_create(owner=request.user.id)
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


# Website reference: reportlab.com\docs/reportlab-userguide.pdf
# Step 1 type in terminal: pip install reportlab
# Step 2 follow these steps below:

# Download data "myclass" in csv file
@login_required
def download_class_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=myclass.csv'

    writer = csv.writer(response)

    # The content in the file
    student_data = Payment.objects.filter(siswa__owner=request.user.id)

    # create column in the csv
    writer.writerow(['Siswa', 'Class Name', 'Language', 'Framework', 'Function'])

    # output
    for data in student_data:
        siswa = data.siswa
        kelas_siswa = data.kelas_siswa
        
        writer.writerow([f"{siswa.first_name} {siswa.last_name}", kelas_siswa.name, kelas_siswa.language, kelas_siswa.framework, kelas_siswa.function])
    
    return response


# Download data "myclass" in pdf file
@login_required
def download_class_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()

    # create canvas/blank page
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    # Create the object text
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont("Helvetica", 12)
    
    # The content of the file
    student_data = Payment.objects.filter(siswa__owner=request.user.id)

    # Create the line of the text
    lines = []

    for data in student_data:
        siswa = data.siswa
        kelas_siswa = data.kelas_siswa
        
        lines.append(f"Siswa: {siswa.first_name} {siswa.last_name}")
        lines.append(f"Kelas: {kelas_siswa.name}")
        lines.append(f"Language: {kelas_siswa.language}")
        lines.append(f"Framework: {kelas_siswa.framework}")
        lines.append(f"Function: {kelas_siswa.function}")
        lines.append("---------------------------------------------")

    # Looping
    for baris in lines:
        textobject.textLine(baris)

    # Execute into file
    c.drawText(textobject)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='myclass.pdf')
