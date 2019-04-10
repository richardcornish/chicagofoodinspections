# Settings
# https://docs.djangoproject.com/en/2.2/topics/settings/
# https://docs.djangoproject.com/en/2.2/ref/settings/
# https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


import os

from django.urls import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'fake-key')

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = [
    '.chicagofoodinspections.org',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'accounts',
    'profiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'chicagofoodinspections.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'chicagofoodinspections.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Sites
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = os.environ.get('SITE_ID', 1)


# Auth
# https://docs.djangoproject.com/en/2.2/topics/auth/

AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = reverse_lazy('accounts:login')

LOGIN_REDIRECT_URL = reverse_lazy('accounts:account')

LOGOUT_REDIRECT_URL = reverse_lazy('accounts:login')


# E-mail
# https://docs.djangoproject.com/en/2.2/topics/email/

EMAIL_SUBJECT_PREFIX = ''

DEFAULT_FROM_EMAIL = 'rich@richardcornish.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Heroku
# https://devcenter.heroku.com/articles/django-app-configuration

import django_heroku

django_heroku.settings(locals())


# GeoDjango
# https://docs.djangoproject.com/en/2.2/ref/contrib/gis/

if DEBUG:

    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.spatialite'

    SPATIALITE_LIBRARY_PATH = '/usr/local/lib/mod_spatialite.dylib'

else:

    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

    GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH', '')

    GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH', '')
