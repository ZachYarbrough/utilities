#!/bin/bash
# blur - run blur Docker container on any file or folder

# Check if Docker image exists
if ! docker image inspect blur &> /dev/null; then
    echo "Docker image 'blur' not found. Please build it from your utilities repo and ensure it is cloned."
    exit 1
fi

if [ -z "$1" ]; then
  echo "Usage: blur <file_or_directory> [convert_from] [convert_to]"
  exit 1
fi

# Resolve the absolute path of the input
INPUT="$(realpath "$1")"
CONVERT_FROM="${2:-}"  # defaults to empty if not provided
CONVERT_TO="${3:-}"    # defaults to empty if not provided

# Parent folder to mount into /images
HOST_DIR="$(dirname "$INPUT")"

# Name of the file or folder inside /images
CONTAINER_PATH="/images/$(basename "$INPUT")"

# Run the Docker container
docker run --rm -v "$HOST_DIR":/images blur "$CONTAINER_PATH" "$CONVERT_FROM" "$CONVERT_TO"
