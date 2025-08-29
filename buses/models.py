from django.db import models
from users.models import User

class Bus(models.Model):
    bus_number = models.CharField(max_length=20)
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role__name':'Driver'})
    capacity = models.IntegerField()
    current_lat = models.FloatField(default=0.0)
    current_lng = models.FloatField(default=0.0)
    speed = models.FloatField(default=0.0)
    def __str__(self):
        return self.bus_number
