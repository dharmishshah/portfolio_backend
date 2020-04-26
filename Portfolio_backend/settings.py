"""
Django settings for Portfolio_backend project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import urllib

import mongoengine

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from pip._vendor.urllib3.util import url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_aw(y494jcqpn+u9-#9+*_6*8$*&69e0hzreb36^b(qrcqa@3o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'dharmishshahdjango.herokuapp.com']

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
       'http://localhost:3000',
        'http://dharmishshah.herokuapp.com',
        'http://dharmishshah.com'
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio.apps.PortfolioConfig',
    'corsheaders',
    'rest_framework'
]

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dharmishshahportfolio@gmail.com'
EMAIL_HOST_PASSWORD = 'Blackveins@1'
EMAIL_RECIPIENT = 'dharmish21@gmail.com'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'Portfolio_backend.urls'
CSRF_COOKIE_SECURE = False
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Portfolio_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': 'djongo',
    #     'NAME': 'heroku_9vq5ccvc1344',
    #     'HOST': 'mongodb://heroku_9vq5ccvc12:tt8s1tatubg6ouen22rv98cuf12347@ds257097.mlab.com:57097/heroku_9vq5ccvc123',
    #     'USER': 'heroku_9vq5ccvc123',
    #     'PASSWORD': 'tt8s1tatubg6ouen22rv98cuf712322',
    # }

'default': {
            'ENGINE': 'djongo',
            # 'ENFORCE_SCHEMA': False,
            # 'LOGGING': {
            #     'version': 1,
            #     'loggers': {
            #         'djongo': {
            #             'level': 'DEBUG',
            #             'propogate': False,
            #         }
            #     },
            #  },
            'NAME': 'heroku_9vq5ccvc',
            'CLIENT': {
                'host': 'mongodb://heroku_9vq5ccvc:tt8s1tatubg6ouen22rv98cuf7@ds257097.mlab.com:57097/heroku_9vq5ccvc',
                'port': 57097,
                'username': 'heroku_9vq5ccvc',
                'password': 'tt8s1tatubg6ouen22rv98cuf7',
                'authSource': 'heroku_9vq5ccvc',
                'authMechanism': 'SCRAM-SHA-1'
            }
        }
    }




DATABASES = {
'default': {
            'ENGINE': 'djongo',
            # 'ENFORCE_SCHEMA': False,
            # 'LOGGING': {
            #     'version': 1,
            #     'loggers': {
            #         'djongo': {
            #             'level': 'DEBUG',
            #             'propogate': False,
            #         }
            #     },
            #  },
            'NAME': 'test',
            'CLIENT': {
                'host': 'mongodb+srv://adminUser:adminUser@portfolio-xrxao.mongodb.net/test?retryWrites=true&w=majority',
                'username': 'adminUser',
                'password': 'adminUser',
                'authMechanism': 'SCRAM-SHA-1'
            }
        }
    }


# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'test',
#         'HOST': 'localhost:27017',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


