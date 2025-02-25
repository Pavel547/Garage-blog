from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic

from .models import CarBrand, CarReview

# def index(request):
#     car_reviews_list = CarReview.objects.all()
#     return render(request, 'car_blog/content.html', {'car_reviews_lst': car_reviews_list})

class BrandsViewList(generic.ListView):
    template_name = "car_blog/brands.html"
    context_object_name = "car_brands"
    
    def get_queryset(self):
        return CarBrand.objects.all()
    
class IndexView(generic.ListView):
    template_name = "car_blog/content.html"
    context_object_name = "car_reviews_lst"
    
    def get_queryset(self):
        return CarReview.objects.all()

# def review_detail(request, review_id):
#     review = get_object_or_404(CarReview, pk=review_id)
#     return render(request, 'car_blog/review.html', {'review_detail': review})

class ReviewView(generic.DetailView):
    model = CarReview
    template_name = "car_blog/review.html"
    context_object_name = "review_detail"
