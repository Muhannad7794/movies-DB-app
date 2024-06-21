# Base image
FROM node:18

# Set working directory
WORKDIR /frontend-dockerized

# Install dependencies
COPY package.json /frontend-dockerized/
COPY package-lock.json /frontend-dockerized/
RUN npm install

# Copy project
COPY . /frontend-dockerized/

# Build the project
RUN npm run build

# Serve the application
RUN npm install -g serve
CMD ["serve", "-s", "build"]
