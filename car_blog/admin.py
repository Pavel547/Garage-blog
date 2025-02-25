from django.contrib import admin

from .models import CarBrand, CarReview, FuelType, CarBrandLogo, CarReviewImg

admin.site.register(CarBrand)
admin.site.register(CarReview)
admin.site.register(FuelType)
admin.site.register(CarBrandLogo)
admin.site.register(CarReviewImg)
