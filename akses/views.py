from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import send_mail

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            user.is_active = False
            user.save()

            subject = 'Aktivasi akun anda sekarang!'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })

            # user.email_user(subject, message)
            send_mail(subject, message, 'anggiana0092@gmail.com', [user.email], fail_silently=False)
            
            # login(request, user)
            return redirect('send_activation')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form,})

def send_activation(request):
    return render(request, 'registration/send_activation.html', {})

def activate(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_validated = True
        user.save()

        login(request, user)
        messages.success(request, 'Akun berhasil diaktifkan, silahkan login')
        return redirect('login')
    else:
        messages.error(request, 'Aktivasi akun gagal')
        return redirect('register')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Kamu berhasil login'))
            return(redirect('myprofile'))
        else:
            messages.success(request, ('Login tidak berhasil, ada kesalahan username atau password'))
            return(redirect('login'))
    else:
        return render(request, 'registration/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('Kamu sudah berhasil keluar, silahkan login kembali'))
    return(redirect('login'))



# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Password berhasil diganti')
#             return redirect(reverse('login'))
#         else:
#             messages.success(request, 'Pasword Gagal diganti')
#             return redirect(reverse('change_password'))
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {'form': form})