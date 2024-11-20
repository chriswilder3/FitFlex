from django.urls import path
             # path is a function provided by Django to define URL patterns
from . import views 

from django.conf import settings # Need this to set url where 
                                   # product/item images will be retreived 
                                   # from

from django.conf.urls.static import static # need this for setting
                            # the url which can be used for
                            #  accessing the images in template later.

urlpatterns = [
    # The urlpatterns list is a mandatory variable in a Django app that 
    # contains all the URL-to-view mappings.

    path('items/',views.items, name='items'),
    # The path contains the url pattern that is mapped to its view
    # Here the whole url of request is : <base_url>/items/ which acts
    # as an endpoint of this app/module.
    # The base_url is defined in projects urls.py, so make sure to
    # to route it appropriately.

    path('items/item_details/<int:id>', views.item_details, name='details'),

    # items/items_details/: This part of the URL is static. 
    # It tells Django to match this specific part of the URL path exactly.

    # <int:id>: This part is a dynamic segment. It means that Django 
    # will expect an integer value for id to appear in the URL. The value
    #  will be passed to the corresponding view function as a parameter.
    # Ex: if /items/items_details/5/ is the url, id=5 is passed to view

    path('', views.home, name='home'),

    path('test/', views.test, name='test')

]


if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


