from django.urls import path
             # path is a function provided by Django to define URL patterns
from . import views 

urlpatterns = [
    # The urlpatterns list is a mandatory variable in a Django app that 
    # contains all the URL-to-view mappings.

    path('items/',views.items, name='items')
    # The path contains the url pattern that is mapped to its view
    # Here the whole url of request is : <base_url>/items/ which acts
    # as an endpoint of this app/module.
    # The base_url is defined in projects urls.py, so make sure to
    # to route it appropriately.

]

