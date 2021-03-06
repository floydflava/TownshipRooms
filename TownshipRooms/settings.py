"""
Django settings for TownshipRooms project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tp0dypukbw7op_s9mxd^os!=mb427q5pm9##@*arm5-lwx9vcz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DJANGO_DEBUG', None) == '1' else False

DJANGO_ENV = os.environ.get('DJANGO_ENV','PRODUCTION')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'core_platform',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TownshipRooms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'TownshipRooms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if DJANGO_ENV == "PRODUCTION":
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    #DATABASES['default']['NAME'] = 'development'



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_files"),
]


MEDIA_ROOT = 'media'

STATIC_ROOT = 'static'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

if DJANGO_ENV == "PRODUCTION":

    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

    GS_BUCKET_NAME = 'township-rooms-web-prod'

    GS_AUTO_CREATE_BUCKET = True

    GS_AUTO_CREATE_ACL = 'public-read'

    GS_PROJECT_ID = 'township-rooms'

    GCS_ROOT = "https://storage.googleapis.com/{bucket_name}/".format(
        bucket_name=os.environ.get("GS_BUCKET_NAME", GS_BUCKET_NAME)
    )

    MEDIA_PREFIX = "media"

    STATIC_PREFIX = "static"

    MEDIA_URL = "{gcs_root}{prefix}/".format(
        gcs_root=GCS_ROOT,
        prefix=MEDIA_PREFIX,
    )

    STATIC_URL = "{gcs_root}{prefix}/".format(
        gcs_root=GCS_ROOT,
        prefix=STATIC_PREFIX,
    )
