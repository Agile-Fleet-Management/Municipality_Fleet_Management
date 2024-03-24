#!/bin/bash

git stash

echo "Pulling latest API changes"

git pull

echo "Stopping and removing existing containers"

docker compose down

echo "Building latest changes"

docker compose up -d --build

echo "Deployment complete"