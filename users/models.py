from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    assigned_bus = models.ForeignKey('buses.Bus', on_delete=models.SET_NULL, null=True, blank=True)

    # Override default ManyToMany fields to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # change to avoid clash
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # change to avoid clash
        blank=True,
        help_text='Specific permissions for this user.'
    )
