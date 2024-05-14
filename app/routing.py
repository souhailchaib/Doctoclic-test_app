from .consumers import EventConsumer

# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from django.core.asgi import get_asgi_application


websocket_urlpatterns = [
    path("ws/calendar/", EventConsumer.as_asgi()),
    # Add more WebSocket URL patterns as needed
]


application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(websocket_urlpatterns),
        "http": get_asgi_application(),
        # Add other protocol routes here if needed
    }
)
