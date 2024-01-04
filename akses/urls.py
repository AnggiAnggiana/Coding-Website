from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('send_activation', views.send_activation, name="send_activation"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    # path('', include('django.contrib.auth.urls')),
    # path('signup/', views.signup, name="signup"),
    # path('change_password/', views.change_password, name="change_password"),
]