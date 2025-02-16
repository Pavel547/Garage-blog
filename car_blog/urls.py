from django.urls import path

from . import views

app_name = 'car_blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_id>/review_detail', views.review_detail, name='review_detail'),
]
