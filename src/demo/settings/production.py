from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip_address', 'www.mywebsite.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config(DB_NAME),
        'USER':config(DB_USER),
        'PASSWORD':config(DB_PASSWORD),
        'HOST':'localhost',
         'PORT''
    }
}


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


STRIPE_PUBLIC_KEY =config('STRIPE_P_KEY')
STRIPE_SECRET_KEY =config('STRIPE_S_KEY')