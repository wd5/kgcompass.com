# Create your views here.
#from compass.decorators import render_to
#
#@render_to( 'service/home.html' )
#def home( request ):
#    data = {}
#    return data

from common.views import CommonTemplateView

class ServiceView( CommonTemplateView ):
    template_name = 'service/home.html'

    def get_context_data( self, **kwargs ):
        context = super( ServiceView, self ).get_context_data( **kwargs )
        return context


