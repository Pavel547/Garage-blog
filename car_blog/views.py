from django.shortcuts import render, get_object_or_404
from  django.views.generic import ListView, DetailView

from .models import CarBrand, CarReview

class IndexView(ListView):
    model = CarReview
    template_name = "car_blog/content.html"
    context_object_name = "reviews_list"
    
class BrandsListView(IndexView):
    model = CarBrand
    template_name = "car_blog/brands.html"
    context_object_name = "brands_list"
    
class ReviewDetailView(DetailView):
    model = CarReview
    template_name = "car_blog/review.html"
    context_object_name = "review_details"
    
class BrandDetailView(DetailView):
    model = CarBrand
    template_name = "car_blog/brand.html"
    context_object_name = "brand_details"
