#!/bin/bash

create_symlinks () {
  # Creates symlinks for config files
  ln -s ~/Documents/utilities/fconv/fconv.sh ~/bin/fconv
 
  # Make bash scripts executable
  chmod +x ~/Documents/utilities/fconv/fconv.sh
}

create_symlinks
