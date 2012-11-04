from django.db import models
from django.contrib.auth.models import User
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


class CommonPage( MPTTModel ):
    parent = TreeForeignKey( 'self', null = True, blank = True, related_name = 'children' )
    title_en = models.CharField( max_length = 250 )
    content_en = tinymce_models.HTMLField()
    title_ru = models.CharField( max_length = 250 )
    content_ru = tinymce_models.HTMLField()
    type = models.CharField( max_length = 15, choices = ( ( 'catalog', 'catalog', ), ( 'page', 'page', ), ), default = 'page' )


    class Meta:
        abstract = True

#    class MPTTMeta:
#        order_insertion_by = ['title']

    def __unicode__( self ):
        return self.title_en

#    def slug( self ):
#        return slugify( self.title )
