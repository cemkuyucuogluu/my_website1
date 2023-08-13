#!/bin/sh

python manage.py migrate --noinput

python manage.py createsuperuser --username="admin" --email="cemkuyucuogluu@gmail.com" --no-input

exec "$@"