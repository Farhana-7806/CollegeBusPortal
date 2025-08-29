from django.db import models
from users.models import User
from buses.models import Bus

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role__name':'Student'})
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
