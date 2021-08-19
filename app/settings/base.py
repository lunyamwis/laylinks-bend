"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from datetime import timedelta
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'brooks_insurance_agency_software_2021')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    'graphene_django',
    'django_password_validators',
    'rolepermissions',
    'simple_history',
    'softdelete',
    'django_filters',
    'django_extensions',
    'rest_framework',

    'app.api',
    'app.api.roles',
    'app.api.authentication',
]
SAFE_DELETE_INTERPRET_UNDELETED_OBJECTS_AS_CREATED=True
AUTH_USER_MODEL = 'authentication.User'
ROLEPERMISSIONS_MODULE = "app.api.roles.roles"
GRAPHENE = {
    'SCHEMA': 'app.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': timedelta(days=1),

}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "http://134.209.28.109",
    "http://localhost",
    "http://127.0.0.1"
]

ROOT_URLCONF = 'app.urls'

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

ASGI_APPLICATION = 'app.asgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME','laylinks'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'martin1996-'),
        'HOST': os.getenv('DB_HOST','localhost'),
        'USER': os.getenv('DB_USER','martin'),
        'PORT': '5432',
    }
}
AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# History
SIMPLE_HISTORY_HISTORY_ID_USE_UUID = True
# SIMPLE_HISTORY_HISTORY_CHANGE_REASON_USE_TEXT_FIELD=True

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django_password_validators.password_history.UniquePasswordsValidator',
    }
]
# If you want, you can change the default hasher for the password history.
DPV_DEFAULT_HISTORY_HASHER =     'django_password_validators.password_history.hashers.HistoryHasher'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django_password_validators.password_character_requirements.password_validation.PasswordCharacterValidator',
        'OPTIONS': {
            'min_length_digit': 1,
            'min_length_alpha': 4,
            'min_length_special': 1,
            'min_length_lower': 1,
            'min_length_upper': 1,
            'special_characters': "[~!@#$%^&*()_+{}\":;'[]"
        }
    }
]
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


PASSWORD_RESET_URL = os.getenv('PASSWORD_RESET_URL', '')

# Celery configurations
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', '')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', '')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Agency
MAIL_CAPTION=os.getenv('MAIL_CAPTION', '')

# send grid credentials
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
DEFAULT_FROM_EMAIL=os.getenv("DEFAULT_FROM_EMAIL", "")
EMAIL_SENDER=os.getenv('EMAIL_SENDER', '')
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Twilio
TWILIO_ACC_SID = os.getenv('TWILIO_ACC_SID', '')
TWILIO_ACC_AUTH_TOKEN = os.getenv('TWILIO_ACC_AUTH_TOKEN', '')
TWILIO_NOTIFY_SERVICE_SID = os.getenv('TWILIO_NOTIFY_SERVICE_SID', '')
GOOGLE_APPLICATION_CREDENTIALS=os.getenv('GOOGLE_APPLICATION_CREDENTIALS', "")
