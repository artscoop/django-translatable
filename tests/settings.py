# This is a Django settings file for django-translatable unit testing

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

INSTALLED_APPS = (
    # tested package
    'translatable',
    # test packages
    'package',
    'models',
    'admin',
)

# Activate code coverage report if required packages are available
try:
    import coverage
    import testcoverage
except ImportError:
    pass
else:
    TEST_RUNNER = 'testcoverage.test_runner.TestCoverageTestRunner'
    TESTCOVERAGE_APPS = (
        'translatable',
    )

USE_I18N = True

LANGUAGES = (
    ('en', "English"),
    ('es', "Spanish"),
)

