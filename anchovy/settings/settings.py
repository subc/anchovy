# -*- coding:utf-8 -*-
# Django settings for anchovy project.
import os
import sys
from .pathutil import abs_parent_path

# プロジェクトのルートディレクトリへのパスを取得
ROOT_PATH = abs_parent_path(__file__, up_level=1)

# インポートのパスを設定
sys.path.append(os.path.join(ROOT_PATH, 'submodule'))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DB_USER = 'root'
DB_PASS = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'anchovy',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# LocalMemCache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT' : 3600,
        'OPTIONS' : {'MAX_ENTRIES': 30000,},
        },
    }

# Redis
REDIS_DATABASES = {
    'default': {
        'HOST': 'localhost',
        'PORT': '6379',
        'DB': '0',
        }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Japan'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ja'

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
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i^w0l8tue6(j2c-je=!&%pquviiuc*aisy^!qofy!4fl19%uja'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.eggs.Loader',
    # 端末によってロードするテンプレートを変更するローダー
    'mobilejp.template.loaders.mobile_switch.Loader',
    # app内のtemplatesディレクトリを見るローダー ※ gsocial
    'django.template.loaders.app_directories.Loader',


)


TEMPLATE_DIRS = (
    ROOT_PATH + '/templates/website/pc',
)

# PC用
PC_TEMPLATE_DIRS = (
    ROOT_PATH + '/templates/website/pc',
)

# SP用
SMARTPHONE_TEMPLATE_DIRS = (
    ROOT_PATH + '/templates/website/sp',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # UserAgentから端末情報判別し保存する
    'mobilejp.middleware.mobile.UserAgentMobile2Middleware',


)




ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'settings.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
)

INSTALLED_APPS += (
    'module.download',
    'module.common',
    'module.ita',
    'module.res',
)

# submodules
INSTALLED_APPS += (
    # 'gsocial',
    # 'horizontalpartitioning',
    'mobilejp',
    # 'kome',
    # 'gamelog',  # モデル
    # 'gtoolkit.analytics',  # タグ
    # 'gtoolkit.animation',  # タグ
    # 'gtoolkit.pager',  # タグ
    # 'gtoolkit.image2',  # タグ
    # テンプレートタグのエラーでもエラーメールが飛ぶようになる。
    # 'gtoolkit.error_mail.templatetags',
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
