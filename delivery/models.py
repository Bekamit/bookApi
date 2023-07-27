from django.db import models

# Create your models here.

class city_id(models.Model):
    name_city = models.CharField(max_length=20)
    days_delivery = models.PositiveIntegerField()

class client(models.Model):
    name_client = models.CharField(max_length=20)
    city_id = models.ForeignKey(city_id, models.PROTECT)
    email = models.EmailField(max_length=254)