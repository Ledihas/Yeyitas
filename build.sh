#!/usr/bin/env bash
# Exit on error
set -o errexit


# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations

python manage.py showmigrations
python manage.py migrate --noinput

python manage.py createsuperuser

echo "Creando superusuario..."
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input --email $DJANGO_SUPERUSER_EMAIL --username $DJANGO_SUPERUSER_USERNAME
fi


echo "Tareas de construcción completadas."

