from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import CarBrand, CarReview

def index(request):
    try:
        car_brands_list = CarBrand.objects.all()
    except CarBrand.DoesNotExist:
        return Http404('Car brands list is empty')
    return render(request, 'car_blog/content.html', {'car_brands_lst': car_brands_list})


