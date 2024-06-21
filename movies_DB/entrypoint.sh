#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    python manage.py migrate --settings=movies_DB.settings_prod
else
    python manage.py migrate
fi

# Collect static files
echo "Collecting static files..."
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    python manage.py collectstatic --noinput --settings=movies_DB.settings_prod
else
    python manage.py collectstatic --noinput
fi

# Start server
echo "Starting server..."
exec "$@"
