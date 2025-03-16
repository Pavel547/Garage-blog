from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import CarBrand, CarReview

from .forms import BrandForm, BrandLogoForm, CarReviewForm, ReviewImgsForm, CarProsFormSet, CarConsFormSet

def home(request):
    return render(request, "car_blog/home.html")
    
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
        logoform = BrandLogoForm(request.POST, request.FILES)
        
        if brandform.is_valid() and logoform.is_valid():
            brand = brandform.save()
            
            logo = logoform.save(commit=False)
            logo.brand = brand
            logo.save()
            
            return redirect("car_blog:brands_list")
    else:
        brandform = BrandForm()
        logoform = BrandLogoForm()
        
    context = {
        "brandform": brandform,
        "logoform": logoform,
    }    
        
    return render(request, "car_blog/brand/brand_form.html", context)
        
def create_review(request):
    if request.method == "POST":
        reviewform = CarReviewForm(request.POST)
        imgsform = ReviewImgsForm(request.POST, request.FILES)
        prosformset = CarProsFormSet(request.POST)
        consformset = CarConsFormSet(request.POST)
        
        if reviewform.is_valid() and imgsform.is_valid() and prosformset.is_valid() and consformset.is_valid():
            review = reviewform.save()
            
            imgs = imgsform.save(commit=False)
            imgs.car_review = review
            imgs.save()
            
            prosformset.instance = review
            consformset.instance = review
            
            prosformset.save()
            consformset.save()
            
            return redirect("car_blog:reviews_list")
    else:
        reviewform = CarReviewForm()
        imgsform = ReviewImgsForm()
        prosformset = CarProsFormSet()
        consformset = CarConsFormSet()
        
    context = {
        "reviewform": reviewform,
        "imgsform": imgsform,
        "carprosformset": prosformset,
        "carconsformset": consformset,
    }
    return render(request, "car_blog/review/review_form.html", context)
