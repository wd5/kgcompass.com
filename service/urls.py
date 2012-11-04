from django.conf.urls import patterns, include, url

urlpatterns = patterns( 'service',
    url( r'^$', 'views.home', name = 'service-home' ),
 )
