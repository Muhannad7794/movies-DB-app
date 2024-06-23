# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables for Django
ARG DB_NAME
ARG PASSWORD
ARG DB_ROOT_PASSWORD
ARG USER
ARG AZURE_ACCOUNT_NAME
ARG AZURE_ACCOUNT_KEY
ARG AZURE_MEDIA_CONTAINER
ARG AZURE_STATIC_CONTAINER
ARG ALLOWED_HOSTS
ARG CORS_ALLOWED_ORIGINS
ARG HOST
ARG PORT
ARG SECRET_KEY
ARG DEBUG
ARG TMDB_API_KEY

ENV DB_NAME=$DB_NAME \
    PASSWORD=$PASSWORD \
    DB_ROOT_PASSWORD=$DB_ROOT_PASSWORD \
    USER=$USER \
    AZURE_ACCOUNT_NAME=$AZURE_ACCOUNT_NAME \
    AZURE_ACCOUNT_KEY=$AZURE_ACCOUNT_KEY \
    AZURE_MEDIA_CONTAINER=$AZURE_MEDIA_CONTAINER \
    AZURE_STATIC_CONTAINER=$AZURE_STATIC_CONTAINER \
    ALLOWED_HOSTS=$ALLOWED_HOSTS \
    CORS_ALLOWED_ORIGINS=$CORS_ALLOWED_ORIGINS \
    HOST=$HOST \
    PORT=$PORT \
    SECRET_KEY=$SECRET_KEY \
    DEBUG=$DEBUG \
    TMDB_API_KEY=$TMDB_API_KEY

# Set the working directory in the container
WORKDIR /movies-app

# Copy the current directory contents into the container at /movies-app
COPY . /movies-app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project
COPY movies_DB/ /movies-app/

# Copy entrypoint script and set permissions
COPY movies_DB/entrypoint.sh /movies-app/
RUN chmod +x /movies-app/entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/movies-app/entrypoint.sh"]
