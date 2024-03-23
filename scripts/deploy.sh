#!/bin/bash

echo "Pulling latest API changes"

git pull

echo "Building latest changes"

<<<<<<< Updated upstream
docker-compose up -d --build
=======
docker compose up -d --build
>>>>>>> Stashed changes

echo "Deployment complete"