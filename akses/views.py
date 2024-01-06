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
from decouple import config

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

            subject = 'Activate your account now!'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })

            send_mail(subject, message, config('EMAIL_HOST_USER'), [user.email], fail_silently=False)
            
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
        messages.success(request, 'Your account already activated, please login')
        return redirect('login')
    else:
        messages.error(request, 'Activate account is failed')
        return redirect('register')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("now you're logged in"))
            return(redirect('myprofile'))
        else:
            messages.success(request, ('Login failed, your username or password is wrong'))
            return(redirect('login'))
    else:
        return render(request, 'registration/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out, please login again"))
    return(redirect('login'))

