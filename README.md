# Utilities

## Overview
This repository contains a set of small, reusable scripts and tools designed to make development tasks faster and easier.  

Current utilities include:

- **fconv** – Dockerized image converter that converts JPG/PNG files to WebP.

Each utility lives in its own subfolder with instructions for usage and setup.  

Feel free to clone the entire repo or use individual utilities as needed.


## Installation

Clone repo into new directory. (I like to keep these scripts in `~/Documents/utilities`)
```
# Use SSH (if set up)...
git clone git@github.com:ZachYarbrough/utilities.git ./utilities

# Or use HTTPS and switch remotes later.
git clone https://github.com/ZachYarbrough/utilities.git ./utilities
```

Run the below command to create symlinks in the Home directory for all config files in the repo as well as install homebrew and its dependencies.
```
cd ./utilities
bash ./install.sh
```
