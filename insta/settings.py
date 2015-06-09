"""
Django settings for insta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join
from easy_thumbnails.conf import Settings as thumbnail_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if __name__ in ('settings', 'insta.settings'):
    import sys
    sys.path.insert(0, join(BASE_DIR, 'insta'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7dkzasdd3by1p7431*j243s611&!xxsagko*bee1&by!)mt2#%w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
TESTING = 'test' in sys.argv

ALLOWED_HOSTS = ('10.1.1.123', )


# Application definition

INSTALLED_APPS = (
    'grappelli',
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # additional apps

    # insta apps
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

ROOT_URLCONF = 'insta.urls'
WSGI_APPLICATION = 'insta.wsgi.application'

# Database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insta',
        'USER': 'insta',
        'PASSWORD': 'eXKce0VV',
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

MEDIA_URL = '/static/img/'
MEDIA_ROOT = 'static/img/'

TEMPLATE_DIRS = (join(BASE_DIR, 'insta', 'templates'), )

# rainbow tests
TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner'

# error reports
SERVER_EMAIL = 'notification@insta.com'
ADMINS = (('Maks', 'samael500@gmail.com'), )

# email settings
DEFAULT_FROM_EMAIL = 'no-reply@insta.com'
EMAIL_HOST = 'debugmail.io'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'samael500@gmail.com'
EMAIL_HOST_PASSWORD = 'd6b2d120-0e94-11e5-9683-afa17037bc5a'

try:
    from settings_local import *  # noqa
except ImportError:
    pass
