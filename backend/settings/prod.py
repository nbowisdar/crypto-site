from .base import *
from os import getenv
from decouple import config
SECRET_KEY = config('SECRET_KEY')

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'crypto1324.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5432',
    }
}
