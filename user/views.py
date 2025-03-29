from django.shortcuts import render, redirect

from .forms import RegistrationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('user:login')
    else:
        form = RegistrationForm()
    return render(request, "accounts/registration.html",{"registrationform": form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email, password)
        if user is not None:
            login(request, user)
            return redirect('user:profile')
        else:
            error_message = "User doesn't exist, please register on the website."
    return render(request, "accounts/login.html", {'error': error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('accounts/login')
    else:
        return redirect('home')
