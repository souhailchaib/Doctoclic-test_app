import os
import django

from uvicorn import Config, Server
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_app.settings")


django.setup()


application = get_default_application()


# Uvicorn ASGI configuration
config = Config(
    app=application,
    loop="asyncio",
    http="h11",
    ws="websockets",
)

uvicorn_server = Server(config)
