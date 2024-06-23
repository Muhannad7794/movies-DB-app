#!/bin/bash

# Source the .env file if it exists
if [ -f /movies-app/.env ]; then
    set -a
    source /movies-app/.env
    set +a
fi

# Debugging: Print environment variables to confirm they are loaded
echo "Starting the application in $DJANGO_ENVIRONMENT mode..."

# Check for production environment and prepare the app
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    echo "Running database migrations..."
    python manage.py migrate --noinput
    echo "Collecting static files..."
    python manage.py collectstatic --noinput --clear
    echo "Starting Gunicorn server on port 8000..."
    exec gunicorn movies_DB.wsgi:application --bind 0.0.0.0:8000 --log-level debug --capture-output --timeout 120
else
    echo "Starting Django development server..."
    exec python manage.py runserver 0.0.0.0:8000
fi
