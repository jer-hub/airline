from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destinations")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

class Passenger(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    flight = models.ManyToManyField(Flight, related_name="passengers")

