#!/bin/bash

# Install Docker
sudo apt update
sudo apt install -y docker.io

# Build Docker image
docker build -t in-memory-file-system .

# Run Docker container
docker run -it in-memory-file-system
