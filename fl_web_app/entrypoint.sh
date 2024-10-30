#!/bin/sh

# Applica le migrazioni Django
python manage.py makemigrations
python manage.py migrate


# Avvia Gunicorn
exec "$@"