from django import forms

from .models import CarBrand, BrandLogo, CarReview, CarPros, CarCons, ReviewImgs

class BrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ["car_brand", "brand_description"]
        
class BrandLogoForm(forms.ModelForm):
    class Meta:
        model = BrandLogo
        fields = ["logo_img"]
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = "__all__"
        
        
