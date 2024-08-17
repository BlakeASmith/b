#!/bin/bash

sudo pacman -S python-pipx --noconfirm
pipx ensurepath
#sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
