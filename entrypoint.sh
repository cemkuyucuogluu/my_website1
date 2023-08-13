#!/bin/sh

python manage.py migrate --noinput

python manage.py createsuperuser --username="$DJANGO_SUPER_USERNAME" --email="$DJANGO_SUPER_USER_EMAIL" --no-input

exec "$@"


