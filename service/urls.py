from django.conf.urls import patterns, include, url
from . views import ServiceHomeView, ServicePageView

urlpatterns = patterns( 'service',
    url( r'^$', ServiceHomeView.as_view(), name = 'service-home' ),
    url( r'^(?P<id>\d+)(?:\-(?P<slug>[\w\-]+))?$', ServicePageView.as_view(), name = 'service-page' ),
 )
