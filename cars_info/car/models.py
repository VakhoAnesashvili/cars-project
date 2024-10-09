from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    model_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)]
    )
    engine = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=20)
    odometer = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', default='car_images/default.png', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} {self.odometer}"
