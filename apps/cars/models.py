from django.db import models
from core.models import BaseModel


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    v = models.FloatField()
    body = models.CharField(max_length=30)
    price = models.IntegerField()