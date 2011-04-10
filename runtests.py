#!/usr/bin/env python

import os
import sys

try:
    from django import VERSION as DJANGO_VERSION
except ImportError:
    print >> sys.stderr, "ERROR: You have no Django installed in your Python path"
    sys.exit(1)

if DJANGO_VERSION[0] < 1 or DJANGO_VERSION[1] < 2:
    print >> sys.stderr, "ERROR: Required Django version is 1.2 or greater"
    sys.exit(1)

try:
    import testcoverage
except ImportError:
    print >> sys.stderr, "WARNING: You have no django-testcoverage package installed."
    print >> sys.stderr, "........ Code coverage won't be reported."

PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT_PATH, 'tests'))
sys.path.insert(1, PROJECT_ROOT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

def delete_pyc():
    CLEANED_DIRS = (
        'tests',
        'translatable',
    )
    for dir in CLEANED_DIRS:
        for root, dirs, files in os.walk(os.path.join(PROJECT_ROOT_PATH, dir)):
            for file in files:
                if file[-4:] == '.pyc':
                    os.remove(os.path.join(root, file))

if __name__ == '__main__':
    delete_pyc()
    from django.core import management
    management.call_command('test')

