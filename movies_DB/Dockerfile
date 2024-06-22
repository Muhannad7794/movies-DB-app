# Movies_DB_app/movies_DB/Dockerfile

# Base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /movies-app

# Copy the .env file from the root directory to the work directory
COPY ../.env /movies-app/

# Copy requirements.txt and install dependencies
COPY movies_DB/requirements.txt /movies-app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project
COPY movies_DB/ /movies-app/

# Copy entrypoint script and set permissions
COPY movies_DB/entrypoint.sh /movies-app/entrypoint.sh
RUN chmod +x /movies-app/entrypoint.sh

# Apply database migrations
RUN if [ "$DJANGO_ENVIRONMENT" = "production" ]; then \
    python manage.py migrate --settings=movies_DB.settings_prod; \
    else \
    python manage.py migrate; \
    fi

# Collect static files
RUN if [ "$DJANGO_ENVIRONMENT" = "production" ]; then \
    python manage.py collectstatic --noinput --settings=movies_DB.settings_prod; \
    else \
    python manage.py collectstatic --noinput; \
    fi

# Expose port 8000
EXPOSE 8000

# Run entrypoint script
ENTRYPOINT ["/movies-app/entrypoint.sh"]

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
