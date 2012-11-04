from django.contrib import admin

from common.admin import CommonPageAdmin
from . models import InfoPage

class InfoPageAdmin( CommonPageAdmin ):
    pass

admin.site.register( InfoPage, InfoPageAdmin )
