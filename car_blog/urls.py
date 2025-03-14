from django.urls import path
from . import views

app_name = 'car_blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('review-list/', views.ReviewsListView.as_view(), name="reviews_list"),
    path('brands-list/', views.BrandsListView.as_view(), name="brands_list"),
    path('<int:pk>/review-details/', views.ReviewDetailView.as_view(), name="review_details"),
    path('<int:pk>/brand-details/', views.BrandDetailView.as_view(), name="brand_details"),
    path('add-car-logo/', views.add_brand, name="add_brand")
]
