# Django settings for compass project.

import os

IN_PRODUCTION = True

try:
    from local_settings import *
except ImportError, e:
    pass

DEBUG = not IN_PRODUCTION
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ( 
    ( 'Dan Tyan', 'dan.tyan@gmail.com' ),
 )

MANAGERS = ADMINS



if IN_PRODUCTION:
    DOCROOT = '/home/zokisoft/www/kgcompass/'
    APPPATH = '/home/zokisoft/django/kgcompass/'
else:
    DOCROOT = '/home/dan/www/django/compass/'
    APPPATH = '/home/dan/www/django/compass/'


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

_ = lambda s: s
LANGUAGES = ( 
    ( 'en', _( u'English' ) ),
    ( 'ru', _( u'Russian' ) ),
 )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = DOCROOT + 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = DOCROOT + 'static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ( 
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APPPATH + 'info/static',
    APPPATH + 'service/static',
    APPPATH + 'main/static',
    APPPATH + 'common/static',
    APPPATH + 'compass/static',
    APPPATH + 'region/static',
 )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
 )



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
 )

MIDDLEWARE_CLASSES = ( 
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
 )

ROOT_URLCONF = 'compass.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'compass.wsgi.application'

TEMPLATE_DIRS = ( 
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APPPATH + 'info/templates',
    APPPATH + 'service/templates',
    APPPATH + 'main/templates',
    APPPATH + 'common/templates',
    APPPATH + 'compass/templates',
    APPPATH + 'region/templates',
 )

TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
#    'compass.context_processors.custom',
#    'blog.context_processors.common',
 )

INSTALLED_APPS = ( 

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'grappelli',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',


    'mptt',
    'tinymce',
    'slugify',
    'localeurl',

    'common',
    'service',
    'info',
    'region',
 )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#--------------------------------
# debug toolbar
#--------------------------------
if DEBUG:
    MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware', )
    INSTALLED_APPS += ( 'debug_toolbar', )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }


#--------------------------------
# bootstrap form
#--------------------------------

INSTALLED_APPS += ( 'bootstrapform', )


# ## SOUTH: BEGIN
INSTALLED_APPS += ( 'south', )
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False
# ## SOUTH: END


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

TINYMCE_JS_ROOT = STATIC_URL + 'js/tiny_mce/'
TINYMCE_JS_URL = STATIC_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,autoresize",
    'theme': "advanced",
    'theme_advanced_resizing' : 'true',
    'width':'600',

}


INTERNAL_IPS = ( '127.0.0.1', )


STATUS_CHOICES = ( 
    ( 'active', 'active' ),
    ( 'inactive', 'inactive' ),
    ( 'draft', 'draft' ),
    ( 'deleted', 'deleted' ),
 )

SEND_BROKEN_LINK_EMAILS = True

DEFAULT_FROM_EMAIL = 'compass.caeg@gmail.com'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = "587"
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'craZZyDemon357x'
EMAIL_USE_TLS = True

USE_DJANGO_JQUERY = True


LOCALE_INDEPENDENT_PATHS = ( 
    r'^/admin/',
#    r'^/games/',
#    r'^/ajax/',
 )
LOCALEURL_USE_ACCEPT_LANGUAGE = True
LOCALE_REDIRECT_PERMANENT = False

#CSRF_COOKIE_SECURE = True


#INSTALLED_APPS += ( 'compressor', )
#STATICFILES_FINDERS += (
#    'compressor.finders.CompressorFinder',
# )
#COMPRESS_ENABLED = True
#COMPRESS_OUTPUT_DIR = 'cache'
