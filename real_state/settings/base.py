
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# env = environ.Env(
#     DEBUG=(bool,False)
# )

# environ.Env.read_env(BASE_DIR/".env")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#oj(1a@tv7#g!+r0m((s55#b5o=d9!l)i^jqg7j$$$qew5q!kw'
# SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = env("DEBUG")

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

SITE_ID = 1

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "djoser",
    "rest_framework_simplejwt",
    'rest_framework.authtoken'
    
]

LOCAL_APPS = [
    "apps.profiles",
    "apps.users",
    "apps.ratings",
    "apps.common"
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL='users.CustomUser'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real_state.urls'

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

WSGI_APPLICATION = 'real_state.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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

REST_FRAMEWORK={
    "DEFAULT_AUTHENTICATION_CLASSES":(
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
    # "DEFAULT_AUTHENTICATION_CLASSES":(
    #     "apps.users.authenticaion.MultiTokenAuthentication",
    # ),
}

from datetime import timedelta
SIMPLE_JWT = {
    # "AUTH_HEADER_TYPES":(
    #     "Bearer",
    #     'JWT',
    # ),
    # 'ACCESS_TOKEN_LIFETIME':timedelta(minutes=120),
    # 'REFRESH_TOKEN_LIFETIME':timedelta(days=1),
    # 'SIGNING_KEY':'SIGNING_KEY',
    # 'AUTH_HEADER_NAME':"HTTP_AUTHORIZATION",
    # 'AUTH_TOKEN_CLASSES':("rest_framework_simplejwt.tokens.AccessToken",),
}

# DJOSER={
#     "LOGIN_FIELD":'email',
#     'USER_CREATE_PASSWORD_RETYPE':True,
#     'EMAIL_CHANGED_EMAIL_CONFIRMATION':True,
#     'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
#     'SEND_CONFIRMATION_EMAIL':True,
#     'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
#     'EMAIL_RESET_CONFIRM_URL':'email/reset/confirm/{uid}/{token}',
#     'SET_PASSWORD_RETYPE':True,
#     'PASSWORD_RESET_CONFIRM_RETYPE':True,
#     'ACTIVATION_URL':'active/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL':True,
#     'SERIALIZERS':{
#         'user_create':'appps.users.serializers.CustomUserCreationSerializer',
#         'user':'appps.users.serializers.CustomUserSerializer',
#         'current_user':'appps.users.serializers.CustomUserSerializer',
#         'user_delete':'djoser.serializers.UserDeleteSerializer',

#     }
    
# }
import logging
import logging.config

from django.utils.log import DEFAULT_LOGGING

logger = logging.getLogger(__name__)

LOG_LEVEL = 'INFO'

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            },
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "logs/real_estate.log",
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
            "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)
