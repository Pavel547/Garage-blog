from django.urls import path

from . import views

app_name = 'car_blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/review_detail/', views.ReviewView.as_view(), name='review_detail'),
]
