#!/bin/bash

# Start Nginx
nginx

# Start Django server
cd /app/conclusions/
python3 manage.py runserver 0.0.0.0:8000