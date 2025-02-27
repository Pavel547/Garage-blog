from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'car_blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('brands_list/', views.BrandsListView.as_view(), name="brands_list"),
    path('<int:pk>/review_details/', views.ReviewDetailView.as_view(), name="review_details"),
    path('<int:pk>/brand_details/', views.BrandDetailView.as_view(), name="brand_details")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

