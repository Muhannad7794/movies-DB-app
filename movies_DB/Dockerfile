# Base image
FROM python:3

# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /movies-app

# Install dependencies
COPY movies_DB/requirements.txt /movies-app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project
COPY movies_DB/ /movies-app/

# Copy entrypoint script and set permissions
COPY movies_DB/entrypoint.sh /movies-app/
RUN chmod +x /movies-app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Run entrypoint script
ENTRYPOINT ["/movies-app/entrypoint.sh"]