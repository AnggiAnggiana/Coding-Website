from django.contrib import admin
from .models import Course
from .models import Class
from .models import Student
from .models import Payment

# admin.site.register(Course)
# admin.site.register(Class)
# admin.site.register(Student)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'lecture', 'kelas',)
    ordering = ('name',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    search_fields = ('name', 'language', 'framework', 'function',)
    list_display = ('name', 'language', 'framework', 'function',)
    ordering = ('name',)
    list_filter = ('name', 'language', 'framework', 'function',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email', 'level', 'profesi',)
    list_display = ('first_name', 'last_name','email', 'level', 'profesi',)
    ordering = ('first_name',)
    list_filter = ('first_name', 'email', 'level', 'profesi',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ('siswa', 'kelas_siswa',)
    list_display = ('siswa', 'kelas_siswa',)
    list_filter = ('siswa', 'kelas_siswa',)