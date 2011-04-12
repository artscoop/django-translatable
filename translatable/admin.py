from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class TranslationInlineModelAdmin(object):
    """
    Base class for inline model admin classes, merged with Stacked- or TabularInline.
    """
    verbose_name = _("Translation")
    verbose_name_plural = _("Translations")
    max_num = len(settings.LANGUAGES)
    extra = 1

class TranslationStackedInline(TranslationInlineModelAdmin, admin.StackedInline):
    """
    Base class for inline model admin for your translations. The only things you have to do
    is to add the `model` attribute poiting to your TranslationModel in its descendant and
    add its descendant to `inlines` list of your TranslatableModel admin class.
    """
    pass

class TranslationTabularInline(TranslationInlineModelAdmin, admin.TabularInline):
    """
    Base class for inline model admin for your translations. The only things you have to do
    is to add the `model` attribute poiting to your TranslationModel in its descendant and
    add its descendant to `inlines` list of your TranslatableModel admin class.
    """
    pass

