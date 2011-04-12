from django.utils import unittest
from django.utils import functional
from django.contrib import admin as django_admin
from translatable import admin

class TranslationInlineModelAdminTestCase(unittest.TestCase):

    def test_has_proper_attributes(self):
        self.assertTrue(hasattr(admin.TranslationInlineModelAdmin, 'verbose_name'))
        self.assertTrue(hasattr(admin.TranslationInlineModelAdmin, 'verbose_name_plural'))
        self.assertTrue(hasattr(admin.TranslationInlineModelAdmin, 'max_num'))
        self.assertTrue(hasattr(admin.TranslationInlineModelAdmin, 'extra'))

    def test_are_names_translatable(self):
        self.assertIsInstance(admin.TranslationInlineModelAdmin.verbose_name, functional.Promise)
        self.assertIsInstance(admin.TranslationInlineModelAdmin.verbose_name_plural, functional.Promise)

class TranslationStackedInlineTestCase(unittest.TestCase):

    def test_has_proper_acestors(self):
        self.assertTrue(issubclass(admin.TranslationStackedInline, admin.TranslationInlineModelAdmin))
        self.assertTrue(issubclass(admin.TranslationStackedInline, django_admin.StackedInline))

class TranslationTabularInlineTestCase(unittest.TestCase):

    def test_has_proper_acestors(self):
        self.assertTrue(issubclass(admin.TranslationTabularInline, admin.TranslationInlineModelAdmin))
        self.assertTrue(issubclass(admin.TranslationTabularInline, django_admin.TabularInline))

