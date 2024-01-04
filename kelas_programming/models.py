from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField('Email')
    address = models.TextField(blank=True)
    owner = models.IntegerField(blank=False, default=1) #Dibuat hanya ketika membuat my profile page
    kelasku = models.ManyToManyField('Class', blank=True) #Dibuat untuk menambahkan Class untuk student yg berbeda-beda
    LEVEL_CHOICES = [
        ('pemula', 'Pemula'),
        ('menengah', 'Menengah'),
        ('expert', 'Expert'),
    ]

    level = models.CharField(max_length=30, choices=LEVEL_CHOICES, default='pemula')

    PROFESI_CHOICES = [
        ('programmer-fulltime', 'Programmer-Fulltime'),
        ('programmer-freelancer', 'Programmer-Freelancer'),
        ('non-programmer', 'Non-Programmer'),
    ]

    profesi = models.CharField(max_length=30, choices=PROFESI_CHOICES, default='programmer-fulltime')

    def __str__(self):
        # return self.first_name + ' ' + self.last_name
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    name = models.CharField('Kelas', max_length=120)
    language = models.CharField('Language',max_length=120)
    framework = models.CharField('Framework', max_length=120)
    function = models.CharField('Function', max_length=120)
    link = models.URLField('Link')
    definition = models.TextField('Definition')
    photo = models.ImageField('Photo', blank=True, null=True, upload_to='class_photo/')
    video = models.FileField('Video', blank=True, null=True, upload_to='class_video/')

    def __str__(self):
        return self.name

# Untuk payment kelas yg dipilih
class Payment(models.Model):
    siswa = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    kelas_siswa = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)


class Course(models.Model):
    name = models.CharField('Programming Course', max_length=120)
    date = models.DateTimeField('Course Date')
    lecture = models.CharField('Lecturer', max_length=120)
    kelas = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    myclass = models.ManyToManyField(Student, blank=True, null=True)

    def __str__(self):
        return self.name



# Untuk Profile User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    activation_key = models.CharField(max_length=255, default=1, unique=True)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User, dispatch_uid="save_new_user_profile")
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()

    



