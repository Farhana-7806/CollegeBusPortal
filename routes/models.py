from django.db import models
from buses.models import Bus

class Stop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    order = models.IntegerField()

class Route(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=100)
    stops = models.ManyToManyField(Stop, blank=True)
