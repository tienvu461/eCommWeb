from .base import *
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecommdb',
        'USER': 'ecomm',
        'PASSWORD': 'ecomm123',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

# print sql to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    },
}
