#!/bin/bash

(cd bootstrap && ./bootstrap.py)
(cd ansible && ansible-playbook -c local -i 127.0.0.1, main.yml)

