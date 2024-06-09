#!/bin/sh

/wait-for-it.sh sample-server:8000 --timeout=60 --strict -- echo "Backend is up"

nginx -g 'daemon off;'