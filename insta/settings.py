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
    'geoposition',
    # insta apps
    'index',
    'cards',
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

# youtube api settings
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
YOUTUBE_UPLOAD_SCOPE = 'https://www.googleapis.com/auth/youtube.upload'
# secure connection settings
YOUTUBE_REFRESH_TOKEN = '<secret>'
YOUTUBE_CLIENT_ID = '<secret>'
YOUTUBE_CLIENT_SECRET = '<secret>'
# youtube video upload settings
YOUTUBE_CHUNKSIZE = -1
YOUTUBE_CATEGORY_ID = 19
YOUTUBE_TITLE = 'I am discoverer {coord}'
YOUTUBE_TAGS = 'discover, travel, worl, pioner, selfie'
YOUTUBE_VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')
YOUTUBE_PRIVACY_STATUS = YOUTUBE_VALID_PRIVACY_STATUSES[1]

try:
    from settings_local import *  # noqa
except ImportError:
    pass

try:
    if 'TRAVIS' in os.environ:
        from settings_travis import *  # noqa
except ImportError:
    pass
