from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('send_activation', views.send_activation, name="send_activation"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    # path dibawah untuk signup&login with google
    path('login/', views.login, name='login'),
]