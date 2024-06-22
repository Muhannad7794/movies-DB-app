from .settings import *
import os
from django.core.exceptions import ImproperlyConfigured

DEBUG = False
ALLOWED_HOSTS = ["*"]  

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

# Azure storage settings for production
AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
AZURE_MEDIA_CONTAINER = os.getenv("AZURE_MEDIA_CONTAINER")
AZURE_STATIC_CONTAINER = os.getenv("AZURE_STATIC_CONTAINER")

if (
    not AZURE_ACCOUNT_NAME
    or not AZURE_ACCOUNT_KEY
    or not AZURE_MEDIA_CONTAINER
    or not AZURE_STATIC_CONTAINER
):
    raise ImproperlyConfigured("Azure storage settings are not configured properly.")

# Debugging: Print environment variables to confirm they are loaded
print(f"AZURE_ACCOUNT_NAME: {AZURE_ACCOUNT_NAME}")
print(f"AZURE_ACCOUNT_KEY: {AZURE_ACCOUNT_KEY}")
print(f"AZURE_MEDIA_CONTAINER: {AZURE_MEDIA_CONTAINER}")
print(f"AZURE_STATIC_CONTAINER: {AZURE_STATIC_CONTAINER}")

DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"

AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/"
STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Azure Storage settings
AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = os.getenv("AZURE_STATIC_CONTAINER")
