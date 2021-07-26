from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


# Create your views here.




def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, f'This username is already in use. Please supply a different username.')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.warning(request, f'This email address is already in use. Please supply a different email address.')
                return redirect('register')

            elif username == "":
                messages.warning(request, f'This username is empty. Please enter username.')
                return redirect('register')

            elif email == "":
                messages.info(request, f'This email address is empty. Please enter email address.')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, birthday=birthday, gender=gender)
                user.save()
                messages.success(request, f'Thank you for creating account. {username}')
                return redirect('signin')

        else:
            messages.warning(request, f'Password do not match!')
            return redirect('register')
        return redirect('/')


    else:
        return render(request, "register.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.warning(request, f'Invalid username/password!')
            return redirect('signin')

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    messages.success(request, f'Logged out sucessfully!')
    return redirect('signin')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account have been updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'profile.html', context)

