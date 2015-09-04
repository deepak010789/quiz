"""
Django settings for quiz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

from os.path import join, dirname, realpath
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))    

#os.path.dirname(os.path.dirname(__file__))

#MEDIA_ROOT = join(BASE_DIR, "media")
#MEDIA_URL = "/media/"
#ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'mne(g9637h$@lbl@d!4#xg8ppkhbe^!d*x&)^c2tsix9p0gue('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'textarea',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quiz.urls'

WSGI_APPLICATION = 'quiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tinymce',
        'USER': 'tinymce',
        'PASSWORD': 'tinymce',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages"
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
)

STATIC_URL = "/static/"
STATIC_ROOT = join(BASE_DIR, "static")
#STATICFILES_DIRS = (
#    "/home/hadoolytics-deepak/workspace/tinymce/quiz/quiz/staticfiles/",
#)

STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

TEMPLATE_DIRS = (
    "/home/hadoolytics-deepak/workspace/tinymce/quiz/textarea/templates/",
    "/home/hadoolytics-deepak/workspace/tinymce/quiz/quiz/static/django_tinymce/",
)

#TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True
#TINYMCE_JS_URL = os.path.join(STATIC_ROOT, "tiny_mce/plugins/equationeditor/tinymce.min.js")
#TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "static/tiny_mce")
#TINYMCE_JS_URL = os.path.join(STATIC_ROOT,'static/tiny_mce/tiny_mce_src.js')
#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,spellchecker,paste,searchreplace",
#    'theme': "modern",
#}

