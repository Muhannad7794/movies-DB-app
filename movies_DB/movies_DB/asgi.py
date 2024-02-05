import os
import django
from channels.routing import ProtocolTypeRouter, get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies_DB.settings.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": get_default_application(),
    }
)
