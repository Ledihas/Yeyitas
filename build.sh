#!/usr/bin/env bash
# Exit on error
set -o errexit

# Update pip
pip3 install --upgrade pip

# Install dependencies
pip3 install -r requirements.txt

# Install Djongo and Pymongo if not in requirements
pip3 install --upgrade djongo #pymongo
python -m pip install "pymongo[aws]"

# Convert static asset files
rm -rf staticfiles/
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Create superuser if CREATE_SUPERUSER is set
if [[ $CREATE_SUPERUSER == "true" ]]; then
    echo "Creando superusuario..."
    python manage.py createsuperuser --no-input --email $DJANGO_SUPERUSER_EMAIL --username $DJANGO_SUPERUSER_USERNAME
fi

echo "Tareas de construcción completadas."
