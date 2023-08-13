#!/bin/sh

python manage.py migrate --noinput

python manage.py createsuperuser --username="admin" --email="cemkuyucuogluu@gmail.com" --password='623262@@' --no-input

exec "$@"


