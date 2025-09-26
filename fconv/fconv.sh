#!/bin/bash
# fconv - run file-converter Docker container on any file or folder

# Check if Docker image exists
if ! docker image inspect fconv &> /dev/null; then
    echo "Docker image 'fconv' not found. Please build it from your utilities repo and ensure it is cloned."
    exit 1
fi

if [ -z "$1" ]; then
  echo "Usage: fconv <file_or_directory>"
  exit 1
fi

# Resolve the absolute path of the input
INPUT="$(realpath "$1")"

# Parent folder to mount into /images
HOST_DIR="$(dirname "$INPUT")"

# Name of the file or folder inside /images
CONTAINER_PATH="/images/$(basename "$INPUT")"

# Run the Docker container
docker run --rm -v "$HOST_DIR":/images fconv "$CONTAINER_PATH"
