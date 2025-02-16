from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import CarBrand, CarReview

def index(request):
    car_reviews_list = CarReview.objects.all()
    return render(request, 'car_blog/content.html', {'car_reviews_lst': car_reviews_list})

def review_detail(request, review_id):
    review = get_object_or_404(CarReview, pk=review_id)
    return render(request, 'car_blog/review.html', {'review_detail': review})
