"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.normpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '*4^hyb59n=nuz9*4=qg(7jcioe4+%2(4$5b+3wlmb0l@3wxrnd'
#
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Application definition
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
INSTALLED_APPS = (
   
    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
     'django.contrib.messages',
    'django.contrib.staticfiles',
     'account',
     'django.contrib.admin',
    'reports',
    'reviewer',
    'django_tables2',
    'xhtml2pdf',
    'django_messages',
    'django.contrib.auth',
    #'django.contrib.sessions'

)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    # 'django.middleware.common.CommonMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
SITE_ID = 1

ROOT_URLCONF = 'mysite.urls'
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
               'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                 'django_messages.context_processors.inbox',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 'default': {
    #   'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.environ.get('DATABASE_NAME', ''),
    #     'USER': os.environ.get('DATABASE_USER', ''),
    #     'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
    #     'HOST': os.environ.get('DATABASE_HOST', ''),
    #     'PORT': os.environ.get('DATABASE_PORT', ''),
    # }
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )

}


#Django's Authentication Libraries
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL='/static/'
ADMIN_MEDIA_PREFIX = '/media/'
