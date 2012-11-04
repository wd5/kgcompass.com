from django.contrib import admin

from common.admin import CommonPageAdmin
from . models import ServicePage

class ServicePageAdmin(CommonPageAdmin):
    pass

admin.site.register( ServicePage, ServicePageAdmin )
