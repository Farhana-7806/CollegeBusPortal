from django.urls import re_path
from .consumers import BusLocationConsumer

websocket_urlpatterns = [
    re_path(r'ws/bus/(?P<bus_id>\w+)/$', BusLocationConsumer.as_asgi()),
]
