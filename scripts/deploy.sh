#!/bin/bash

echo "Resetting local changes"

git reset --hard HEAD

echo "Pulling latest API changes"

git pull

echo "Building latest changes"

docker compose up -d --build

echo "Deployment complete"