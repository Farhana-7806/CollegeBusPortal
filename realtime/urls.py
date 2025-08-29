from django.urls import path
from .views import bus_map

urlpatterns = [
    path('map/', bus_map, name='bus_map'),
]
