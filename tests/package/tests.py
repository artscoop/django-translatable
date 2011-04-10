from django.utils import unittest
import translatable

class PackageTestCase(unittest.TestCase):

    def test_package_version_format(self):
        self.assertRegexpMatches(translatable.__version__, r'^\d+\.\d+\.\d+$',
                                 "Wrong package version format")

