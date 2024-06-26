#!/bin/sh

# Update package list and install Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Start Docker service and enable it to start on boot
sudo systemctl start docker
sudo systemctl enable docker

# Add the current user to the Docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify Docker installation
docker --version
