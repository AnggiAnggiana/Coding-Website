# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Student
from .models import Class
from .models import Course
from .models import Payment
from django.contrib.auth.models import User


# Membuat form untuk data siswa
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('profile_image','first_name', 'last_name', 'email', 'address', 'profesi', 'level')
        labels = {
            'profile_image': '',
        }

        # Styling form
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First_Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last_Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'profesi': forms.Select(attrs={'class': 'form-select'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
        }

    profesi = forms.ChoiceField(choices=Student.PROFESI_CHOICES)
    level = forms.ChoiceField(choices=Student.LEVEL_CHOICES)

# Membuat form untuk Class/kelas
class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields =('name', 'language', 'framework', 'function', 'link')
        labels = {
            'name': '',
            'language': '',
            'framework': '',
            'function': '',
            'link': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama kelas'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bahasa Pemrograman'}),
            'framework': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Framework'}),
            'function': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Function (Frontend / Backend / Database)'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link'}),
        }


# Membuat form untuk Course
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'date', 'lecture', 'kelas', 'description', 'myclass')
        labels = {
            'name': '',
            'date': 'YYYY-MM-DD HH:MM:SS',
            'lecture': '',
            'description': '',
            'myclass': 'Student',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Course'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'lecture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lecture'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'myclass': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Student'}),
        }

# VERSI UDAH JADI TAPI TAMPILAN JELEK
# Untuk payment kelas yg dipilih siswa
# class PaymentForm(ModelForm):
#     class Meta:
#         model = Payment
#         fields = ('siswa', 'kelas_siswa')
        
#         widgets = {
#             # 'siswa': forms.TextInput(attrs={'class': 'form-control'}),
#         }
        
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         kelas_id = kwargs.pop('kelas_id', None)
#         super(PaymentForm, self).__init__(*args, **kwargs)
        
#         # Hanya menampilkan data siswa yg sedang login
#         self.fields['siswa'].instance = Student.objects.filter(owner=user.id)
        
#         # Set nilai default ke siswa yg login
#         default_siswa = Student.objects.get(owner=user.id)
#         self.initial['siswa'] = default_siswa.id
        
#         # Hanya menampilkan data kelas yg dipilih
#         self.fields['kelas_siswa'].instance = Class.objects.filter(id=kelas_id)
#         self.initial['kelas_siswa'] = kelas_id


# VERSI BING
class PaymentForm(ModelForm):
    siswa = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    kelas_siswa = forms.ModelChoiceField(queryset=Class.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    
    class Meta:
        model = Payment
        fields = ('siswa', 'kelas_siswa')
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        kelas_id = kwargs.pop('kelas_id', None)
        super(PaymentForm, self).__init__(*args, **kwargs)
        
        # Hanya menampilkan data siswa yg sedang login & kelas yg dipilih
        self.fields['siswa'].queryset = Student.objects.filter(owner=user.id)
        self.fields['kelas_siswa'].queryset = Class.objects.filter(id=kelas_id)
        
        # Hanya menampilkan data siswa yg sedang login & kelas yg dipilih
        siswa_instance = Student.objects.filter(owner=user.id).first()
        kelas_instance = Class.objects.filter(id=kelas_id).first()
        
        if siswa_instance:
            self.fields['siswa'].initial = siswa_instance
            
        if kelas_instance:
            self.fields['kelas_siswa'].initial = kelas_instance


