"""
local Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
#from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'PORT' : '5432',
        'HOST' : 'localhost',
        'NAME' : 'django_development',
        'USER' : 'newuser',
        'PASSWORD' : 'newuser' 
               }
              }  
