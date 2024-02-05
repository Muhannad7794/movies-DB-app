from .settings import *


DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Development database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "movies_db",
        "USER": os.getenv("USER"),
        "PASSWORD": os.getenv("PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
        "OPTIONS": {"ssl": {"ca": os.getenv("ca")}},
    },
}
