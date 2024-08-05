#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations
python manage.py migrate

echo "Creando superusuario..."
python - <<END
import os
import django
from django.contrib.auth import get_user_model

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyectoD.settings")  
django.setup()

# Crea el superusuario
#User = get_user_model()
#User.objects.create_superuser('jorge', 'jorge.abreu@gmail.com', 'titi1234')
END

echo "Tareas de construcción completadas."

