from django.db import models
from django.utils.html import strip_tags
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models
from slugify import slugify
from urlparse import urlparse


# Create your models here.

if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules( [], ["^tinymce\.models.\HTMLField"] )


class RegionPage(MPTTModel):
    parent = TreeForeignKey( 'self', null = True, blank = True, related_name = 'children' )
    type = models.CharField( max_length = 15, choices = ( ( 'catalog', 'catalog', ), ( 'page', 'page', ), ), default = 'page' )

class RegionPageTranslate(models.Model):
    page = models.ForeignKey( RegionPage )
    title = models.CharField( max_length = 250 )
    content = tinymce_models.HTMLField()
    lang = models.CharField( max_length = 2, choices = settings.LANGUAGES, default = 'en' )
