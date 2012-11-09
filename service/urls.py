from django.conf.urls import patterns, include, url
from . views import ServiceView

urlpatterns = patterns( 'service',
    url( r'^$', ServiceView.as_view(), name = 'service-home' ),
 )
