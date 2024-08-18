#!/bin/bash

(cd ansible && ansible-playbook --ask-become-pass -c local -i 127.0.0.1, main.yml)

