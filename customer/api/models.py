from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    gender = models.CharField(max_length=1)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    geo_latitude = models.FloatField()
    geo_longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
