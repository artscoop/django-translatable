#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import os
import translatable

setup(
    name = 'django-translatable',
    packages = ['translatable',],
    version = translatable.__version__,
    description = "Django app providing simple translatable models system",
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    author = "Kossouho",
    author_email = 'artscoop93@gmail.com',
    url = 'https://github.com/artscoop/django-translatable',
    license = 'BSD License',
    platforms = ['OS Independent',],
    install_requires=[
        'Django>=1.8',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
    ]
)
        

