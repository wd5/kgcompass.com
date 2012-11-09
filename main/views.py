# Create your views here.
#from compass.decorators import render_to

from common.views import CommonTemplateView

#@render_to( 'main/home.html' )
#def home( request ):
#    data = {}
#    return data


class HomeView(CommonTemplateView):
    template_name = 'main/home.html'
    
    def get_context_data( self, **kwargs ):
        context = super( HomeView, self ).get_context_data( **kwargs )
        return context
