from django.contrib import admin

from mptt.admin import MPTTModelAdmin

class CommonPageAdmin( MPTTModelAdmin ):
    list_display = ( 'title_en', 'type' )
    search_fields = ( 'title_en', 'title_ru' )

    class Meta:
        abstract = True
