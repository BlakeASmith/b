#!/bin/sh
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
brew update && brew upgrade pipx
