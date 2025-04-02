from django.shortcuts import render, redirect

from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("user:login")
    else:
        form = RegistrationForm()
        return render(request, "accounts/registration.html", {"registrform": form})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email, password)
        if user is not None:
            login(request, user)
            return redirect("car_blog:home")
        else:
            error_message = "User does not exists, please register on the website."
            return render(request, "accounts/login.html", {"error_message": error_message})
    else:
        return render(request, "accounts/login.html")
        
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("user:login")
    else:
        return render(request, "accounts/logout.html")