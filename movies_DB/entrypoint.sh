#!/bin/bash

# Source the .env file
set -a
source /movies-app/.env
set +a

# Debugging: Print environment variables to confirm they are loaded
echo "SECRET_KEY: $SECRET_KEY"
echo "AZURE_ACCOUNT_NAME: $AZURE_ACCOUNT_NAME"
echo "AZURE_ACCOUNT_KEY: $AZURE_ACCOUNT_KEY"
echo "AZURE_MEDIA_CONTAINER: $AZURE_MEDIA_CONTAINER"
echo "AZURE_STATIC_CONTAINER: $AZURE_STATIC_CONTAINER"

# Apply database migrations
echo "Applying database migrations..."
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    echo "Using production settings"
    python manage.py migrate --settings=movies_DB.settings_prod
else
    echo "Using development settings"
    python manage.py migrate
fi

# Collect static files
echo "Collecting static files..."
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    echo "Collecting static files using production settings"
    python manage.py collectstatic --noinput --settings=movies_DB.settings_prod
else
    python manage.py collectstatic --noinput
fi

# Start server
echo "Starting server..."
exec "$@"
