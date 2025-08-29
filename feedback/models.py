from django.db import models
from users.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # Issue / Suggestion
    description = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateTimeField(auto_now_add=True)
