# Base image
FROM node:18

# Set working directory
WORKDIR /frontend-dockerized

# Install dependencies
COPY frontend_movies_db/package.json frontend_movies_db/package-lock.json ./
RUN npm install

# Copy project
COPY frontend_movies_db/ ./

# Build the project
RUN npm run build

# Serve the application
RUN npm install -g serve
CMD ["serve", "-s", "build"]
