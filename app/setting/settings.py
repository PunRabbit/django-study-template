"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

from app.setting.constant import CONSTANT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-sjv5y-0p+m$jr$p5m6gvgo4w_ea79bi!c0#e2alu=#zcx%&j1*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_celery_results",
    "django_celery_beat",
    "app.apps.user",
    "app.container",
    "app.core",
    "app.logs",
    "app.setting",
    "app.util",
    "app.apps.movie"
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'app.util.exception.global_exception_handler.global_exception_handler',
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "app.util.middleware.logging_middleware.LoggingMiddleware",
]

ROOT_URLCONF = CONSTANT.SETTING_MAIN_URL_FILE_PATH

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.setting.wsgi.domain"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": CONSTANT.DATABASE_CONFIG.MARIADB_CONFIG}

CACHES = {"default": CONSTANT.DATABASE_CONFIG.REDIS_CONFIG}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = CONSTANT.TIME_ZONE

USE_I18N = True

USE_TZ = CONSTANT.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CELERY_BROKER_URL = CONSTANT.CELERY_CONFIG.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = CONSTANT.CELERY_CONFIG.CELERY_RESULT_BACKEND
# CELERY_ACCEPT_CONTENT = CONSTANT.CELERY_CONFIG.CELERY_ACCEPT_CONTENT
# CELERY_TASK_SERIALIZER = CONSTANT.CELERY_CONFIG.CELERY_TASK_SERIALIZER
# CELERY_RESULT_SERIALIZER = CONSTANT.CELERY_CONFIG.CELERY_RESULT_SERIALIZER
CELERY_TIMEZONE = CONSTANT.CELERY_CONFIG.CELERY_TIMEZONE


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            "class": "app.util.middleware.custom_log_file_handler.CustomTimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/django.log"),
            "when": "midnight",
            "backupCount": 0,  # 로그 파일을 최대 30개까지 보관
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
