import random
from django.conf import settings
from django.views.generic import TemplateView
# Create your views here.

class CommonTemplateView( TemplateView ):

    def get_context_data( self, **kwargs ):
        cxt = super( CommonTemplateView, self ).get_context_data( **kwargs )
        cxt['random_background'] = random.randrange( 0, 12 )
        cxt['settings'] = settings
        return cxt
