#!/bin/bash
echo "Building latest changes"

docker compose up -d --build

echo "Deployment complete"