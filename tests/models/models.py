from django.db import models
from translatable.models import TranslatableModel, get_translation_model

class Translatable(TranslatableModel):
    pass

class Translation(get_translation_model(Translatable, "translatable")):

    field = models.CharField("field", max_length=20)

    def __unicode__(self):
        return self.field

