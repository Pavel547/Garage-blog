from django.urls import path

from . import views

app_name = 'auto_blog'
urlpatterns = [
    path('', views.index, name='index')
]
