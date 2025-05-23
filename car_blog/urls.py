from django.urls import path
from . import views

app_name = 'car_blog'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('review-list/', views.ReviewsListView.as_view(), name="reviews_list"),
    path('brands-list/', views.BrandsListView.as_view(), name="brands_list"),
    path('<int:pk>/review-details/', views.ReviewDetailView.as_view(), name="review_details"),
    path('<int:pk>/brand-details/', views.BrandDetailView.as_view(), name="brand_details"),
    path('add-car-brand/', views.add_brand_view, name="add_brand"),
    path('create-review/', views.create_review_view, name="create_review"),
]
