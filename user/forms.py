from django import forms

from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    email = forms.EmailField(widget=forms.EmailInput, label="Email")

    class Meta:
        model = User
        fields = ["username", "password", "password_confirm", "email"]
  
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        password_confirm = clean_data.get("password_confirm")
        
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        else:
            return clean_data
