django-translatable
===================

Summary
-------

django-translatable is a package providing base classes for Django models
which content should be translatable into multiple languages. This allows
you to easily create models which translations can be created through Django 
built-in admin site.

**Required Django version is 1.2 or newer.**

Installation
------------

Just::

    $ pip install django-translatable

or::

    $ easy_install django-translatable

There are no additional requirements apart from Django itself.

Tutorial
--------

Quick tutorial is worth a thousand words. Assume we have a blogging application
in Django. Our models could be::

    from django.db import models

    class Category(models.Model):
        name = models.CharField("category", max_length=50, unique=True)

    class Post(models.Model):
        title = models.CharField("title", max_length=100)
        date = models.DateTimeField("date", auto_now_add=True)
        content = models.TextField("content")
        category = models.ForeignKey(Category, related_name='posts', verbose_name="category")

Of course some things are missing, like ``__unicode__()`` methods, but they're not
essential for our tutorial and would only mess things up.

Now imagine our application needs to be internationalized, for example author decided to
write some posts in Hindi, some in English, and others in both languages. Here comes
the django-translatable.

django-translatable provides you base class for two kinds of models. First one is
*translatable model* which is basicly what is beeing translated, eg. ``Category``
or ``Post``. Second one is *translation model* which is base for translations
of given model.

First thing we have to do is decide which fields in each model should be translatable.
Some basic examples:

* **foreign keys** - in most cases relations between models stay same regardless of language,
  for example post category is independent of post's available translations
* **date fields** - things like dates, IPs, numbers etc. also are in most cases
  language-independent
* **text content** - these are commonly translated fields - titles, slugs, post contents

Now we divide echo model fields into separate models::

    from django.db import models

    class Category(models.Model):
        pass

    class CategoryTranslation(models.Model):
        name = models.CharField("category", max_length=50, unique=True)

    class Post(models.Model):
        date = models.DateTimeField("date", auto_now_add=True)
        category = models.ForeignKey(Category, related_name='posts', verbose_name="category")

    class PostTranslation(models.Model):
        title = models.CharField("title", max_length=100)
        content = models.TextField("content")

Now its time to add some magick django-translatable provides::

    from django.db import models
    from translatable.models import TranslatableModel, get_translation_model

    class Category(TranslatableModel):
        pass

    class CategoryTranslation(get_translation_model(Category, "category")):
        name = models.CharField("category", max_length=50, unique=True)

    class Post(TranslatableModel):
        date = models.DateTimeField("date", auto_now_add=True)
        category = models.ForeignKey(Category, related_name='posts', verbose_name="category")

    class PostTranslation(get_translation_model(Post, "post")):
        title = models.CharField("title", max_length=100)
        content = models.TextField("content")

As you see *translatable models* derive from ``TranslatableModel`` class and *translation
models* derive from a class returned by ``get_translation_model()`` function.

Arguments passed to ``get_translation_model()`` are ``translatable_class`` and ``verbose_name``.

* ``translatable_class`` - model class for which this model is translation
* ``verbose_name`` - verbose name of a field connecting translation to its model - this is
  quite useful if you use Django built-in admin site

Last thing we have to do is to set up `LANGUAGES`_ setting. 

Now we can play with our translations using these methods:

* **TranslatableModel.has_translations()**

  Checks if model has any translation available.

* **TranslatableModel.has_translation(language=None)**

  Returns model translation in a language having given language code. If no language code
  is given, current language of Django internationalization system is used.

* **TranslatableModel.get_translation(language=None, fallback=True)**

  Returns model translation in a language having given language code. If no language code
  is given, current language of Django internationalization system is used.

  If ``fallback`` is True (default) first available translation is returned. Languages are
  check in order of ``LANGUAGES`` setting.

  If no translation was found in any of previous steps,
  ``translatable.exceptions.MissingTranslation`` is raised.

* **TranslatableModel.translated(field_name, default=None, language=None, fallback=True)**

  Returns field of translation. Arguments ``language`` and ``fallback`` are
  same as passed to ``get_translation()`` method. If ``get_translation()`` raises
  ``MissingTranslation`` exception, ``default`` value is returned (``None`` for default).

.. _LANGUAGES: http://docs.djangoproject.com/en/1.3/ref/settings/#languages

Admin site integration
----------------------

Assuming we'd like to integrate our blogging app from tutorial with Django built-in admin
site, this is how out ``admin.py`` file could look like::

    from django.contrib import admin
    from django.conf import settings
    from translatable import admin as trans_admin
    from models import *

    class CategoryTranslationInlineAdmin(trans_admin.TranslationTabularInline):
        model = CategoryTranslation

    class CategoryAdmin(admin.ModelAdmin):
        inlines = [CategoryTranslationInlineAdmin,]

    class PostTranslationInlineAdmin(trans_admin.TranslationStackedInline):
        model = PostTranslation

    class PostAdmin(admin.ModelAdmin):
        inlines = [PostTranslationInlineAdmin,]

    admin.site.register(Category, CategoryAdmin)
    admin.site.register(Post, PostAdmin)

Translations are displayed in admin site as inlines below their model.

Author and license
------------------

**Copyright (c) 2011 Mikołaj Siedlarek <mikolaj.siedlarek@gmail.com>**

Distributed on terms of *3-clause BSD license* (AKA *New BSD License*
or *Modified BSD License*). Do you know the `Django BSD license`_? It's
same.

For details conslut :doc:`license`.

.. _`Django BSD license`: http://code.djangoproject.com/browser/django/trunk/LICENSE


