from django.urls import path
from . import views

urlpatterns = [
    # path to show homepage
    path('', views.homepage, name="homepage"),

    # path to show page coding course
    path('list_kelas', views.list_kelas, name="list_kelas"),
    
    # These path for user profile
    path('myprofile/', views.myprofile, name="myprofile"),
    path('myprofile/edit_profile', views.edit_profile, name="edit_profile"),
    
    # Path for search bar
    path('search_kelas', views.search_kelas, name="search_kelas"),
    
    # Path to create new course
    path('list_kelas/add_course', views.add_course, name="add_course",),
    
    # Path to edit the course
    path('list_kelas/edit_course/<course_id>', views.edit_course, name="edit_course"),

    # Path to delete the course
    path('list_kelas/delete_course/<course_id>', views.delete_course, name="delete_course"),

    # Path to download "myclass" data in CSV
    path('list_kelas/kelas/download_kelas_csv', views.download_class_csv, name="download_class_csv"),

    # Path to download "myclass" data in pdf
    path('list_kelas/kelas/download_kelas_pdf', views.download_class_pdf, name="download_class_pdf"),

    # Path to view the class in the course
    path('list_kelas/view_kelas/<kelas_id>', views.view_kelas, name="view_kelas"),

    # Path for the payment
    path('myprofile/payment/<kelas_id>', views.paymentKelas, name="paymentKelas"),

    # Path to view "myclass"
    path('myprofile/myclass', views.myclass, name="myclass"),
    
    # Path to access the content of "myclass"
    path('myprofile/myclass/<kelas_id>', views.class_content, name="class_content"),
]
