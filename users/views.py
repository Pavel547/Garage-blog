from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView

class UserLoginView(LoginView):
    template_name = "registration/login.html"

class UserLogoutView(LogoutView):
    template_name = "registration/logout.html"

class ResetPasswordView(PasswordResetView):
    template_name = "registration/reset_password.html"
