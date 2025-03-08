from django import forms

class BrandForm(forms.Form):
    car_brand = forms.CharField(label='Car brand', max_length=50)
