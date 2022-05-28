from .base import *
from os import getenv
import environ

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')
SECRET_KEY = env('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}
