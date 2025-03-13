from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import CarBrand, CarReview

from .forms import BrandForm, BrandLogoForm

def index(request):
    return render(request, "car_blog/index.html")
    
class ReviewsListView(ListView):
    model = CarReview
    template_name = "car_blog/review/reviews_page.html"
    context_object_name = "reviews_list"
    
class BrandsListView(ListView):
    model = CarBrand
    template_name = "car_blog/brand/brands.html"
    context_object_name = "brands_list"
    
class ReviewDetailView(DetailView):
    model = CarReview
    template_name = "car_blog/review/review.html"
    context_object_name = "review_details"
    
class BrandDetailView(DetailView):
    model = CarBrand
    template_name = "car_blog/brand/brand.html"
    context_object_name = "brand_details"

def add_brand(request):
    if request.method == "POST":
        brandform = BrandForm(request.POST)
        brandlogoform = BrandLogoForm(request.POST, request.FILES)
        if brandform.is_valid() and brandlogoform.is_valid():
            brand = brandform.save()
            
            brandlogoform = brandlogoform.save(commit=False)
            brandlogoform.brand = brand
            brandlogoform.save()
            
            return redirect ('brands_list')
    else:
        brandform = BrandForm()
        brandlogoform = BrandLogoForm()
        
    return render(request, "car_blog/brand/brand_form.html", {"brandform": brandform, "brandlogoform": brandlogoform})
