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

SITE_URL = 'http://revealer.ru'

AUTH_USER_MODEL = 'accounts.InstaUser'
LOGIN_REDIRECT_URL = '/'

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
    'compressor',
    'captcha',
    'social.apps.django_app.default',
    # insta apps
    'accounts',
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
    # social auth middleware
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
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
STATIC_ROOT = 'markup/static/'

MEDIA_URL = '/static/media/'
MEDIA_ROOT = 'markup/static/media/'

# for allow celery file deletions
FILE_UPLOAD_PERMISSIONS = 0o0777

TEMPLATE_DIRS = (join(BASE_DIR, 'insta', 'templates'), )

# compressor settings
COMPRESS_ROOT = join(BASE_DIR, STATIC_ROOT)
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/x-scss', 'django_libsass.SassCompiler'), )
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder', )

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
YOUTUBE_CATEGORY_ID = 19  # travel
YOUTUBE_TITLE = 'I am discoverer {coord}'
YOUTUBE_TAGS = 'discover, travel, worl, pioner, selfie'
YOUTUBE_VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')
YOUTUBE_PRIVACY_STATUS = YOUTUBE_VALID_PRIVACY_STATUSES[0]
# additional youtube settings
YOUTUBE_VIDEO_URL = 'http://youtu.be/{video_id}'
YOUTUBE_VIDEO_EMBED_URL = 'https://www.youtube.com/embed/{video_id}'

# video validation settings
VIDEO_MIME_TYPES = (
    'application/ogg', 'video/quicktime', 'video/mp4', 'video/x-msvideo', 'video/mpeg', 'video/x-ms-wmv')
VIDEO_EXT = ('.ogv', '.mov', '.mp4', '.avi', '.mpg', '.wmv')
VIDEO_MAX_SIZE = 1024 * 1024 * 512  # 512 Mb
VIDEO_MIN_SIZE = 1024 * 1024 * 1    # 1 Mb

# CELERY SETTINGS
BROKER_URL = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ('pickle', 'json', )

# Recapthca settings
RECAPTCHA_PUBLIC_KEY = 'public_key'
RECAPTCHA_PRIVATE_KEY = 'private_key'
NOCAPTCHA = True

# Social auth settings
SOCIAL_AUTH_VK_OAUTH2_KEY = 'key'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'secret'

AUTHENTICATION_BACKENDS = (
    'social.backends.vk.VKOAuth2',
    # ...
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # django default context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # social auth context
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# email settings
DEFAULT_FROM_EMAIL = 'info@revealer.ru'
EMAIL_HOST = 'host'
EMAIL_PORT = 0
EMAIL_HOST_USER = 'user'
EMAIL_HOST_PASSWORD = 'password'


USE_PROXY = False

try:
    from settings_local import *  # noqa
except ImportError:
    pass

try:
    if 'TRAVIS' in os.environ:
        from settings_travis import *  # noqa
except ImportError:
    pass


if TESTING:

    os.environ['RECAPTCHA_TESTING'] = 'True'
    CELERY_ALWAYS_EAGER = True
