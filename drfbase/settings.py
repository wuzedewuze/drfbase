"""
Django settings for drfbase project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&i0*2kfiau2udxqu5!l50fyx%b(p1i3q_gu0!n*-3za0$(sb^@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'snippets.apps.SnippetsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drfbase.urls'

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

WSGI_APPLICATION = 'drfbase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drfbase',
        'USER': 'user',
        'PASSWORD': '274595861',
        'HOST': '192.168.101.130',
        'PORT': '3401',
    },
}
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {#日志格式
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'myformat':{
            'format':'%(asctime)s %(pathname)s:%(lineno)d[%(levelname)s] - %(message)s'
        }
    },
    'filters': {#过滤器
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {#处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {#发送邮件通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],# 仅当 DEBUG = False 时才发送邮件
            'include_html': True,
        },
        'debug': {#记录到日志文件(需要创建对应的目录，否则会出错)
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "/var/log/django/django.log",#日志输出文件
            'maxBytes':1024*1024*5,#文件大小
            'backupCount': 10,#备份份数
            'formatter':'standard',#使用哪种formatters日志格式
        },
        'selflog':{# 自定义日志文件
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "/var/log/django/myself.log",#日志输出文件
            'maxBytes':1024*1024*5,#文件大小
            'backupCount': 10,#备份份数
            'formatter':'myformat',#使用哪种formatters日志格式
        },
        'console':{#输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {#logging管理器
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'myself':{
            'handlers': ['selflog'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}