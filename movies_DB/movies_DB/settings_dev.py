from .settings import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("USER"),
        "PASSWORD": os.getenv("PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
        # "OPTIONS": {"ssl": {"ca": os.getenv("ca")}},
    },
}

# local storage settings for development
MEDIA_ROOT = os.path.join(BASE_DIR, "MEDIA_ROOT")
DIRECTORS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, "directors")
STUDIOS_MEDIA_ROOT = os.path.join(MEDIA_ROOT, "studios")

MEDIA_URL = "/media/"
STATIC_URL = "/static/"
