from django.urls import path
from . import views

app_name = 'car_blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('review_list/', views.ReviewsListView.as_view(), name="reviews_list"),
    path('brands_list/', views.BrandsListView.as_view(), name="brands_list"),
    path('<int:pk>/review_details/', views.ReviewDetailView.as_view(), name="review_details"),
    path('<int:pk>/brand_details/', views.BrandDetailView.as_view(), name="brand_details"),
    path('create_review/', views.create_review, name="create_review"),
]
