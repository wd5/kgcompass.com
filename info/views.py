# Create your views here.
from compass.decorators import render_to

@render_to( 'info/home.html' )
def home( request ):
    data = {}
    return data
