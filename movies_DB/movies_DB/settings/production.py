from .settings import *
import os
from .settings import BASE_DIR

DEBUG = False

# Azure storage settings
DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")
AZURE_STATIC_CONTAINER = os.getenv("AZURE_STATIC_CONTAINER")

# media files settings
MEDIA_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/"

# static files settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = (
    f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_STATIC_CONTAINER}/"
)


ALLOWED_HOSTS = ["movies-db-app.azurewebsites.net"]
CSRF_TRUSTED_ORIGINS = ["https://" + "movies-db-app.azurewebsites.net"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Production database settings
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


# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
