from django.urls import path

from . import views

app_name = 'car_blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('car_brands/', views.BrandsViewList.as_view(), name='car_brands'),
    path('<int:pk>/review_detail/', views.ReviewView.as_view(), name='review_detail'),
]
