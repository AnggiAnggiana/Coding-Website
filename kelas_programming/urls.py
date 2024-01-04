from django.urls import path
from . import views

urlpatterns = [
    # path untuk menunjukkan homepage
    path('', views.homepage, name="homepage"),

    # path untuk menunjukkan page course
    path('list_kelas', views.list_kelas, name="list_kelas"),

    # path untuk page kelas
    path('list_kelas/kelas', views.kelas, name="kelas"),

    # path untuk membuat kelas bisa di klik dan menuju ke spesifik kelas tersebut
    # path('list_kelas/kelas/show_kelas/<kelas_id>', views.show_kelas, name="show_kelas"),
    
    # path dibawah ini untuk profile user
    path('myprofile/', views.myprofile, name="myprofile"),
    path('myprofile/edit_profile', views.edit_profile, name="edit_profile"),
    
    # Dibawah ini adalah path untuk search bar kelas
    path('search_kelas', views.search_kelas, name="search_kelas"),
    
    # Dibawah ini adalah path untuk mengedit kelas(boleh dihapus)
    path('list_kelas/kelas/edit_kelas/<kelas_id>', views.edit_kelas, name="edit_kelas"),
    
    # Dibawah ini adalah path untuk membuat course baru
    path('list_kelas/add_course', views.add_course, name="add_course",),
    
    # Dibawah ini adalah path untuk mengedit course
    path('list_kelas/edit_course/<course_id>', views.edit_course, name="edit_course"),

    # Dibawah ini adalah path untuk menghapus course
    path('list_kelas/delete_course/<course_id>', views.delete_course, name="delete_course"),

    # Dibawah ini adalah path untuk mendownload file csv dari website
    path('list_kelas/kelas/download_kelas_csv', views.download_class_csv, name="download_class_csv"),

    # Dibawah ini adalah path untuk mendownload file pdf dari website
    path('list_kelas/kelas/download_kelas_pdf', views.download_class_pdf, name="download_class_pdf"),

    # path untuk menunjukan page view_kelas
    path('list_kelas/view_kelas/<kelas_id>', views.view_kelas, name="view_kelas"),

    # Path untuk pembayaran kelas
    path('myprofile/payment/<kelas_id>', views.paymentKelas, name="paymentKelas"),

    # path untuk menunjukkan kelas saya
    path('myprofile/myclass', views.myclass, name="myclass"),
    
    # Path untuk menonton content in myClass
    path('myprofile/myclass/<kelas_id>', views.class_content, name="class_content"),
]
