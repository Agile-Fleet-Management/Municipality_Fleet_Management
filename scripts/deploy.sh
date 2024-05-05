
#!/bin/bash
# Exit script on any error
set -e

# Navigate to the correct directory

# Log the current directory
echo "Deploying from directory: $(pwd)"

# Pull the latest changes from the repository
echo "Pulling the latest changes from the git repository..."
git pull
echo "Successfully pulled the latest changes."

# Build and start the Docker containers
echo "Building and starting Docker containers..."
#docker compose  --no-cache
docker compose up -d --build

echo "Docker containers are up and running."

# Log the status of the containers
echo "Current status of Docker containers:"
docker-compose ps

echo "Deployment complete."