from django.core.exceptions import ObjectDoesNotExist

class MissingTranslation(ObjectDoesNotExist):
    pass

