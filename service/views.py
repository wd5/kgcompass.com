# Create your views here.
#from compass.decorators import render_to
#
#@render_to( 'service/home.html' )
#def home( request ):
#    data = {}
#    return data


from django.shortcuts import get_object_or_404

from . models import ServicePage

from common.views import CommonTemplateView

class ServiceHomeView( CommonTemplateView ):
    template_name = 'service/home.html'

    def get_context_data( self, **kwargs ):
        context = super( ServiceHomeView, self ).get_context_data( **kwargs )
        context['catalog'] = ServicePage.objects.all();
        return context

class ServicePageView( CommonTemplateView ):
    template_name = 'service/page.html'

    def get_context_data( self, id, slug, **kwargs ):
        context = super( ServicePageView, self ).get_context_data( **kwargs )
        context['catalog'] = ServicePage.objects.all()
        page = get_object_or_404( ServicePage, pk = id )

        if page.type == 'catalog':
            context['children'] = page.get_children()

        context['page'] = page
        return context
