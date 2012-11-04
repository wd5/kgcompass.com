from django.conf.urls import patterns, include, url

urlpatterns = patterns( 'info',
    url( r'^$', 'views.home', name = 'info-home' ),
 )
