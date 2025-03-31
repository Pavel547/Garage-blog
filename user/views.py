from django.shortcuts import render, redirect

from .forms import RegistrationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('user:login')
    else:
        form = RegistrationForm()
        return render(request, "accounts/registration.html", {'registationform': form})
            

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
