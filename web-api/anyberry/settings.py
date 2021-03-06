"""
Django settings for anyberry project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from os import getenv
from pathlib import Path

from environ import Env

env = Env(
    # Set type casting + default value
    DEBUG=(bool, False)
)
# Read .env file
Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# local + QIWI IPs
ALLOWED_HOSTS = env(
    "ALLOWED_HOSTS", default="localhost localhost:3000 .ngrok.io 127.0.0.1 79.142.16.0/20 195.189.100.0/22 91.232.230.0/23 91.213.51.0/24").split()


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'berries',
    'users',
    'carts',
    'orders',

    # TODO: change cross-origin front-end to same-origin in production
    'corsheaders',
    'djmoney',

    'rest_framework',
    'rest_framework.authtoken',  # token auth
    'django.contrib.sites',  # content for different domains
    'dj_rest_auth',  # DRF auth API
    'dj_rest_auth.registration',  # DRF registration & verification
    'allauth',
    'allauth.account',  # account management
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'anyberry.urls'

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

WSGI_APPLICATION = 'anyberry.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REDIS_URL = env("REDIS_URL")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,  # 0 database
        "KEY_PREFIX": "django",
        "VERSION": 1,
        "TIMEOUT": 300,  # 300 seconds the key is alive
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

DJANGO_REDIS_IGNORE_EXCEPTIONS = True

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_CURRENCY = 'USD'

# Filesystem path to the media storage directory
MEDIA_ROOT = BASE_DIR / 'media/'

# URL prefix for file storage access
MEDIA_URL = 'media/'

AUTH_USER_MODEL = 'users.CustomUser'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        'APP': {
            'client_id': env('VK_APP_ID'),
            'secret': env('VK_APP_SECURE_KEY'),
            'key': '',
        }
    },
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': '',
        }
    },
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SITE_ID = 1

# TODO: change auth headers in production

# cors
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# CORS_REPLACE# CORS_ORIGIN_WHITELIST = (
#     'https://front.bluemix.net/',
#     'front.bluemix.net',
#     'bluemix.net',
# )
_HTTPS_REFERER = True

# TODO: Samesite=None requires Secure cookies attribute

# sessionid
SESSION_COOKIE_HTTPONLY = False  # allow javascript/client access cookies
SESSION_COOKIE_SAMESITE = 'None'  # send cookies to x

# csrftoken
CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://localhost:3000"]
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'None'
# CSRF_COOKIE_DOMAIN = 'bluemix.net'

QIWI_API_TOKEN = env("QIWI_API_TOKEN")
QIWI_P2P_PUBLIC_KEY = env("QIWI_P2P_PUBLIC_KEY")
QIWI_P2P_SECRET_KEY = env("QIWI_P2P_SECRET_KEY")

# Celery and friends (redis as a message broker + result backend)
CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
