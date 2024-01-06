# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Student
from .models import Class
from .models import Course
from .models import Payment
from django.contrib.auth.models import User


# Create form for student data
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

# Create form for class Kelas
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


# Create form for course
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'date', 'lecture', 'kelas', 'description')
        labels = {
            'name': '',
            'date': 'YYYY-MM-DD HH:MM:SS',
            'lecture': '',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Course'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'lecture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lecture'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'kelas': forms.Select(attrs={'class': 'form-control'}),
        }

# Create form for "payment"
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
        
        # Just show student data (login now) & the choosen class
        self.fields['siswa'].queryset = Student.objects.filter(owner=user.id)
        self.fields['kelas_siswa'].queryset = Class.objects.filter(id=kelas_id)
        
        # Just show student data (login now) & the choosen class
        siswa_instance = Student.objects.filter(owner=user.id).first()
        kelas_instance = Class.objects.filter(id=kelas_id).first()
        
        if siswa_instance:
            self.fields['siswa'].initial = siswa_instance
            
        if kelas_instance:
            self.fields['kelas_siswa'].initial = kelas_instance


