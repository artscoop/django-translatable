from django.utils import unittest
import translatable

class PackageTestCase(unittest.TestCase):

    def test_package_version_format(self):
        self.assertRegexpMatches(translatable.__version__, r'^\d+\.\d+\.\d+$',
                                 "Wrong package version format")

    def test_package_version_tuple(self):
        self.assertIsInstance(translatable.VERSION, tuple)
        self.assertEquals(len(translatable.VERSION), 3)

    def test_version_string_and_tuple_same(self):
        self.assertEquals('%d.%d.%d' % translatable.VERSION, translatable.__version__)

