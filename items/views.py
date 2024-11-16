from django.shortcuts import render # used for rendering HTML template
                    # and returning Http Response object, but not in this 
                    # program
from django.http import HttpResponse
                    # used to send http responses(HTML, JSON, text) back to
                    # the browser/ client
                
from django.template import loader
                # django.template package and its loader module provide
                # Django's template system. They facilitate the use of 
                # templates for dynamically rendering HTML or other content.

# Create your views here.
def sample( request ):     # request object is instance of Http request and
                    # contains infn like method(GET),headers,query params etc
    
    return HttpResponse('<h1> Hello World </h1>')
                    # sends basic text response. Content-Type of the 
                    # response defaults to "text/html" unless specified.


def items(request):
    itemTemplate = loader.get_template('items.html')
                # Retrieves a template file named items.html located in 
                # the TEMPLATES directories as configured in the settings.py 
                # Django searches for the file in the that directory.

    return HttpResponse( itemTemplate.render())
                # The render method of the template object processes the loaded
                # HTML template and returns a string containing HTMl content

                # This string containg HTML content is wrapped as HttpResponse
                # and passed to browser which will unpack into HTML

                # In further views we will see render() completely
         # render() method takes two arguments:
         
                # context (optional): A dictionary that contains the 
                # dynamic data to replace placeholders (variables) in the
                # template.

                # request (optional but recommended): The HTTP request 
                # object, which provides additional context to the 
                # template (for things like URL reversing and accessing 
                # user information).
