from django.db import models
from django.core import validators as V

from apps.auto_parks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=15, unique=True, validators=[
        V.MinLengthValidator(3), V.MaxLengthValidator(15)
    ])
    grad_year = models.IntegerField(default=2000)
    n_seats = models.IntegerField()
    body_type = models.CharField(max_length=10, blank=True)
    engine_cap = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
