from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from .models import CarBrand, BrandLogo, CarReview, CarPros, CarCons, ReviewImgs

class BrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ["car_brand", "brand_description"]
        
class BrandLogoForm(forms.ModelForm):
    class Meta:
        model = BrandLogo
        fields = ["logo_img"]
        
class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = "__all__"

    widgets = {
        "fuel": forms.CheckboxSelectMultiple(),
    }

class ReviewImgsForm(forms.ModelForm):
    class Meta:
        model = ReviewImgs
        fields = ["review_imgs"]    

class CarProsForm(forms.ModelForm):
    class Meta:
        model = CarPros
        fields = ["text"]
  
class CarConsForm(forms.ModelForm):
    class Meta:
        model = CarCons
        fields = ["text"]
        
CarProsFormSet = forms.inlineformset_factory(CarReview, CarPros, form=CarProsForm, extra=5, can_delete=True)
CarConsFormSet = forms.inlineformset_factory(CarReview, CarCons, form=CarConsForm, extra=5, can_delete=True)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=forms.TextInput)
        password = forms.CharField(widget=forms.PasswordInput)
