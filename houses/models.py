from django.db import models

# Create your models here.

class House(models.Model):

  """House Model"""

  name = models.CharField(max_length=140)
  price_per_night = models.PositiveBigIntegerField()
  description = models.TextField()
  isBooked = models.BooleanField(default=True)
  address = models.CharField(max_length=140)

  def __str__(self):
    return self.name

