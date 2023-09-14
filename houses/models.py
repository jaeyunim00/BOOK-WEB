from django.db import models

# Create your models here.

class House(models.Model):
    
    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    isBooked = models.BooleanField()
    
