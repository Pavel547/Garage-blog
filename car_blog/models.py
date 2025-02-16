from django.db import models
from django.utils import timezone

class CarBrand(models.Model):
    brand = models.CharField(max_length=50, unique=True)
    brand_description = models.TextField(blank=True)
    
    def __str__(self):
        return self.brand
    
class CarReview(models.Model):
    
    FUEL_CHOICE = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    
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
    fuel = models.CharField(max_length=50 ,choices=FUEL_CHOICE, blank=True)
    type = models.CharField(max_length=50, choices=CAR_TYPES, blank=True)
    horsepower = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    proc = models.TextField(help_text="Advantages of the car")
    cons = models.TextField(help_text="Disadvantages of the car")
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
