import datetime
from django.db import models
from django.core import validators

from apps.autoparks.models import AutoParkModel

# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'

    brand = models.CharField(max_length=30, validators=(
        validators.MaxLengthValidator(30),
        validators.MinLengthValidator(2)
    ))
    price = models.IntegerField(validators=(validators.MinValueValidator(100), validators.MaxValueValidator(1000000)))
    year = models.IntegerField(validators=(validators.MinValueValidator(1990), validators.MaxValueValidator(datetime.datetime.now().year)))
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)