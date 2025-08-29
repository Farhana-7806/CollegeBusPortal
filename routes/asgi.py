import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import apps.realtime.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_bus_portal.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.realtime.routing.websocket_urlpatterns
        )
    ),
})
