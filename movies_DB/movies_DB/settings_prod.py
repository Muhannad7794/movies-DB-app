from .settings import *

DEBUG = False
ALLOWED_HOSTS = ["your-app-name.herokuapp.com"]

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

# Azure storage settings
DEFAULT_FILE_STORAGE = "storages.backends.azure_storage.AzureStorage"
STATICFILES_STORAGE = "storages.backends.azure_storage.AzureStorage"
AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"

# Static files (CSS, JavaScript, images)
MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/"
STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/"

# set static root
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
