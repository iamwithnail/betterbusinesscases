"""
Django settings for ajax_demo project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-3x$q65bl9&2y-a83w5_+*vp@w8*fxg23x@+s&(**z!+&3dcb9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'color_liker',
    'case',
    'spreadsheet',
    'dashboard',
    'highcharts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

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

APPEND_SLASH = True

TEMPLATE_DIRS = (
    '/Users/chris/django/bbc/ajax_demo/color_liker/templates',
    '/Users/chris/django/bbc/ajax_demo/color_liker/templates/',
    '../color_liker/templates',
    '../case/templates'
)

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'businesscase',
        'USER': 'businesscase',
        'PASSWORD': 'businesscase',
        'HOST': "localhost",  # Empty for localhost through domain sockets or
                              # '127.0.0.1' for localhost through TCP.
        'PORT': '',           # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

SPREADSHEET_MAIN = 'summarydata.xlsx'

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    #Put strings here, like "/home/html/static" or "C:/www/django/static".
    #Always use forward slashes, even on Windows.
    #Don't forget to use absolute paths, not relative paths.
    ("assets", BASE_DIR + "/static"),
    os.path.join('static'),
)
