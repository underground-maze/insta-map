# Local settings
import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Turn debug mode on
DEBUG = True
TEMPLATE_DEBUG = True

# Database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'insta.sqlite3'),
    }
}
