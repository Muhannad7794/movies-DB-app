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

# start the server
echo "Starting server..."
exec "$@"
