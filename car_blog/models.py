from django.db import models
from django.utils import timezone

class CarBrand(models.Model):
    car_brand = models.CharField(max_length=50, unique=True)
    brand_description = models.TextField(blank=True)
    
    def __str__(self):
        return self.car_brand
    
class CarBrandLogo(models.Model):
    brand = models.OneToOneField(CarBrand, on_delete=models.CASCADE, related_name="logo")
    brand_logo = models.ImageField(upload_to='car_logo', blank=True)
    
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
    pros = models.TextField(help_text="Advantages of the car")
    cons = models.TextField(help_text="Disadvantages of the car")
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    
class CarReviewImg(models.Model):
    car_review = models.ForeignKey(CarReview, on_delete=models.CASCADE, related_name="car_img")
    car_img = models.ImageField(upload_to='car_img',blank=True,)
    
    def __str__(self):
        return f"{self.car_review.title} Img's"
    
