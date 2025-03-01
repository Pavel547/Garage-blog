from django.db import models
from django.utils import timezone

class CarBrand(models.Model):
    car_brand = models.CharField(max_length=50, unique=True)
    brand_description = models.TextField(blank=True)
    
    def __str__(self):
        return self.car_brand

class BrandLogo(models.Model):
    brand = models.OneToOneField(CarBrand, on_delete=models.CASCADE, related_name="brand_logo")
    logo_img = models.ImageField(upload_to='brand_logos', blank=True)
    
    def __str__(self):
        return f"{self.brand.car_brand} Logo"

class FuelType(models.Model):
    FUEL_CHOICE = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICE)
    
    def __str__(self):
        return self.fuel_type

class CarReview(models.Model):
    
    CAR_TYPES = [
        ('Convertible','Convertible'),
        ('Coupe','Coupe'),
        ('Crossover','Crossover'),
        ('Electric','Electric'),
        ('Hybrid','Hybrid'),
        ('Luxury','Luxury'),
        ('Sedan','Sedan'),
        ('Sports Car','Sports Car'),
        ('SUV','SUV'),
        ('Truck','Truck'),
        ('Van / Minivan','Van / Minivan'),
        ('Wagon / Hatchback','Wagon / Hatchback'),
    ]
    
    title = models.CharField(max_length=150)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_reviews')
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    content = models.TextField()
    engine = models.CharField(max_length=50)
    fuel = models.ManyToManyField(FuelType, blank=True)
    type = models.CharField(max_length=50, choices=CAR_TYPES, blank=True)
    horsepower_min = models.PositiveIntegerField()
    horsepower_max = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class CarPros(models.Model):
    car_review_pros = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="pros")
    text = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f"{self.text}"
    
class CarCons(models.Model):
    car_review_cons = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="cons")
    text = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f"{self.text}"
    
class ReviewImgs(models.Model):
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="car_review_imgs")
    review_imgs = models.ImageField(upload_to='review_imgs', blank=True)
    
    def __str__(self):
        return f"{self.car_review.title} Review img's"
