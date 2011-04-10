from django.utils import unittest
from django.utils.translation import activate as activate_language
import translatable
from models import Translatable, Translation

class BaseClassesTestCase(unittest.TestCase):

    def test_is_translatable_model_abstract(self):
        try:
            abstract = translatable.models.TranslatableModel()
            abstract.save()
        except:
            pass
        else:
            self.fail("TranslatableModel class should be an abstract model")

class EmptyTranslatableModelTestCase(unittest.TestCase):

    def setUp(self):
        self.model = Translatable()
        self.model.save()

    def test_default_unicode(self):
        with self.assertRaises(translatable.exceptions.MissingTranslation):
            unicode(self.model)

    def test_has_translations(self):
        self.assertFalse(self.model.has_translations())

    def test_has_translation(self):
        self.assertFalse(self.model.has_translation())
        self.assertFalse(self.model.has_translation('en'))

    def test_get_translation(self):
        with self.assertRaises(translatable.exceptions.MissingTranslation):
            self.model.get_translation()
        with self.assertRaises(translatable.exceptions.MissingTranslation):
            self.model.get_translation('en')
        with self.assertRaises(translatable.exceptions.MissingTranslation):
            self.model.get_translation('en', False)

    def test_translated(self):
        self.assertIsNone(self.model.translated('field'))
        self.assertEquals(self.model.translated('field', 31337), 31337)
        self.assertEquals(self.model.translated('field', 31337, 'en'), 31337)
        self.assertEquals(self.model.translated('field', 31337, 'en', False), 31337)

class BasicTranslatableModelTestCase(unittest.TestCase):

    def setUp(self):
        # Translatable
        self.model = Translatable()
        self.model.save()
        # English translation
        self.translation_en = Translation()
        self.translation_en.model = self.model
        self.translation_en.language = 'en'
        self.translation_en.field = "Hello!"
        self.translation_en.save()
        # Spanish translation
        self.translation_es = Translation()
        self.translation_es.model = self.model
        self.translation_es.language = 'es'
        self.translation_es.field = "Hola!"
        self.translation_es.save()

    def tearDown(self):
        self.translation_en.delete()
        self.translation_es.delete()
        self.model.delete()

    def test_has_translations(self):
        self.assertTrue(self.model.has_translations())

    def test_has_translation_default_language(self):
        activate_language('en')
        self.assertTrue(self.model.has_translation())
        activate_language('es')
        self.assertTrue(self.model.has_translation())
        activate_language('it')
        self.assertFalse(self.model.has_translation())

    def test_has_translation_given_language(self):
        self.assertFalse(self.model.has_translation('it'))
        self.assertTrue(self.model.has_translation('en'))
        self.assertTrue(self.model.has_translation('es'))

    def test_get_translation_default_language_no_fallback(self):
        activate_language('en')
        self.assertEquals(self.model.get_translation(fallback=False), self.translation_en)
        activate_language('es')
        self.assertEquals(self.model.get_translation(fallback=False), self.translation_es)
        activate_language('it')
        with self.assertRaises(translatable.exceptions.MissingTranslation):
            self.model.get_translation(fallback=False)

    def test_get_translation_default_language_fallback(self):
        activate_language('en')
        self.assertEquals(self.model.get_translation(), self.translation_en)
        activate_language('es')
        self.assertEquals(self.model.get_translation(), self.translation_es)
        activate_language('it')
        self.assertEquals(self.model.get_translation(), self.translation_en)

    def test_get_translation_given_language_no_fallback(self):
        activate_language('es')
        self.assertEquals(self.model.get_translation('en', fallback=False), self.translation_en)
        activate_language('en')
        self.assertEquals(self.model.get_translation('es', fallback=False), self.translation_es)
        activate_language('en')
        with self.assertRaises(translatable.exceptions.MissingTranslation):
            self.model.get_translation('it', fallback=False)

    def test_get_translation_given_language_fallback(self):
        activate_language('es')
        self.assertEquals(self.model.get_translation('en'), self.translation_en)
        activate_language('en')
        self.assertEquals(self.model.get_translation('es'), self.translation_es)
        activate_language('en')
        self.assertEquals(self.model.get_translation('it'), self.translation_en)

    def test_translated_default_language_no_fallback(self):
        activate_language('en')
        self.assertEquals(self.model.translated('field', fallback=False), "Hello!")
        activate_language('es')
        self.assertEquals(self.model.translated('field', fallback=False), "Hola!")
        activate_language('it')
        self.assertIsNone(self.model.translated('field', fallback=False))
        self.assertEquals(self.model.translated('field', "default", fallback=False), "default")

    def test_translated_default_language_fallback(self):
        activate_language('en')
        self.assertEquals(self.model.translated('field'), "Hello!")
        activate_language('es')
        self.assertEquals(self.model.translated('field'), "Hola!")
        activate_language('it')
        self.assertEquals(self.model.translated('field'), "Hello!")
        self.assertEquals(self.model.translated('field', "default"), "Hello!")

    def test_translated_given_language_no_fallback(self):
        activate_language('es')
        self.assertEquals(self.model.translated('field', language='en', fallback=False), "Hello!")
        activate_language('en')
        self.assertEquals(self.model.translated('field', language='es', fallback=False), "Hola!")
        activate_language('en')
        self.assertIsNone(self.model.translated('field', language='it', fallback=False))
        self.assertEquals(self.model.translated('field', "default", language='it', fallback=False),
                          "default")

    def test_translated_given_language_fallback(self):
        activate_language('es')
        self.assertEquals(self.model.translated('field', language='en'), "Hello!")
        activate_language('en')
        self.assertEquals(self.model.translated('field', language='es'), "Hola!")
        activate_language('es')
        self.assertEquals(self.model.translated('field', language='it'), "Hello!")
        self.assertEquals(self.model.translated('field', "default", language='it'), "Hello!")

