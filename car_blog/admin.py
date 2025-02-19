from django.contrib import admin

from .models import CarBrand, CarReview, FuelType

admin.site.register(CarBrand)
admin.site.register(CarReview)
admin.site.register(FuelType)
