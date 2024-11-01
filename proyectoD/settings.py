"""
Django settings for proyectoD project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#DATABASES = {
#    'default': {
 #       'ENGINE': 'djongo',
  #      # Si necesitas especificarlo
   #     'CLIENT': {
    #        'host': os.environ.get('MONGO_URI')
     #   }
    #}
#}

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'yeyitas',
        'CLIENT': {
            'host': 'mongodb+srv://zahide:1234@database.d7kju.mongodb.net/?retryWrites=true&w=majority&appName=database'
        }
    }
}

try:
    # Attempt to connect to MongoDB
    client = MongoClient(DATABASES['default']['CLIENT']['host'])
    db = client[DATABASES['default']['NAME']]
    print("Conexión exitosa a la base de datos:", DATABASES['default']['NAME'])
except ConnectionFailure as e:
    # Handle connection error
    print(f"Error de conexión a la base de datos {DATABASES['default']['NAME']}: {e}")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #'RENDER' not in os.environ


ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME :
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

"""if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Application definition
"""

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hola',
    's_diurno',
    'terraza',
    'taberna','evento',
    'djongo',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'proyectoD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectoD.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

from django.core.exceptions import ImproperlyConfigured

# Extraer la URL de la base de datos
#db_url = "postgresql://zaza:VeNb2qc8oOhLHRfT1lrapNJpYJ5gu9xq@dpg-cs6u1m56l47c738t9ejg-a.oregon-postgres.render.com/postgre_k7bd"



#DATABASES = {
#    'default': dj_database_url.config(
#        default= 'postgresql://zaza:1234@localhost/postgres',
#        conn_max_age=600
#    )
#}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
