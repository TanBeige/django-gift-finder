#!/usr/bin/env python
from setuptools import setup, find_packages
import django_heroku
setup(name='django-gift-finder',
      version='1.0',
      packages=find_packages(),
      scripts=['manage.py'])