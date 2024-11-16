from django.shortcuts import render # used for rendering HTML template
                    # and returning Http Response object, but not in this 
                    # program
from django.http import HttpResponse
                    # used to send small text http responses

# Create your views here.
def sample( request ):     # request object is instance of Http request and
                    # contains infn like method(GET),headers,query params etc
    
    return HttpResponse('<h1> Hello World </h1>')
                    # sends basic text response. Content-Type of the 
                    # response defaults to "text/html" unless specified.


def items(request):
    