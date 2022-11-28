from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=15)
    grad_year = models.IntegerField()
    n_seats = models.IntegerField()
    body_type = models.CharField(max_length=10)
    engine_cap = models.FloatField()
