# Movies_DB_app/movies_DB/Dockerfile

# Base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /movies-app

# Copy requirements.txt and install dependencies
COPY requirements.txt /movies-app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project
COPY . /movies-app/

# Copy entrypoint script and set permissions
COPY entrypoint.sh /movies-app/entrypoint.sh
RUN chmod +x /movies-app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Run entrypoint script
ENTRYPOINT ["/movies-app/entrypoint.sh"]

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
