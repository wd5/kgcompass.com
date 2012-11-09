from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from . models import RegionPage, RegionPageTranslate

class RegionPageInline( admin.TabularInline ):
    model = RegionPageTranslate
    max_num = 2

class RegionPageAdmin( MPTTModelAdmin ):
    actions_on_top = False

    inlines = [
        RegionPageInline,
    ]


admin.site.register( RegionPage, RegionPageAdmin )
