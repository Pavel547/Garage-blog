from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView
from .forms import RegistrationForm

class UserLoginView(LoginView):
    template_name = "registration/login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loginform"] = context.pop("form")
        return context
    

class UserLogoutView(LogoutView):
    template_name = "registration/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logoutform"] = context.pop("form")
        return context

class ResetPasswordView(PasswordResetView):
    template_name = "registration/reset_password.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resetpassword_form"] = context.pop("form")
        return context
    
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")  
    else:
        form = RegistrationForm()
    return render(request, "registration/registration.html", {"registrationform": form})