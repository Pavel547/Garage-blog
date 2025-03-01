from django.contrib import admin

from .models import CarBrand, CarReview, FuelType, BrandLogo, ReviewImgs
from .models import CarPros, CarCons

admin.site.register(CarBrand)
admin.site.register(CarReview)
admin.site.register(FuelType)
admin.site.register(BrandLogo)
admin.site.register(ReviewImgs)
admin.site.register(CarPros)
admin.site.register(CarCons)
