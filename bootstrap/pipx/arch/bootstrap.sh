#!/bin/bash

sudo pacman -S python-pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
