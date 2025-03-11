from django import forms

from .models import CarBrand, BrandLogo, CarReview, ReviewImgs, FuelType, CarPros, CarCons


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
        fields = [
            "title", "brand", "model", "year",
            "content", "engine", "fuel", "type",
            "horsepower_min", "horsepower_max",
            "price_min", "price_max", "create_at"
        ]
        widgets  = {
            "fuel": forms.CheckboxSelectMultiple()
        }

class CarProsForm(forms.ModelForm):
    class Meta:
        model = CarPros
        fields = ["text"]
        
class CarConsForm(forms.ModelForm):
    class Meta:
        model = CarCons
        fields = ["text"]
        
CarProsFormSet = forms.inlineformset_factory(CarReview, CarPros, form=CarProsForm, extra=3, can_delete=True)
CarConsFormSet = forms.inlineformset_factory(CarReview, CarCons, form=CarConsForm, extra=3, can_delete=True)
        
class ReviewImgForm(forms.ModelForm):
    class Meta:
        model = ReviewImgs
        fields = ["car_review", "review_imgs"]
        
