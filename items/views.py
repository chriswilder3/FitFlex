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

from .models import Item # Import the Item class from the models file

# Create your views here.
def sample( request ):     # request object is instance of Http request and
                    # contains infn like method(GET),headers,query params etc
    
    return HttpResponse('<h1> Hello World </h1>')
                    # sends basic text response. Content-Type of the 
                    # response defaults to "text/html" unless specified.


def sample2(request):
    itemTemplate = loader.get_template('items.html')
                # Retrieves a template file named items.html located in 
                # the TEMPLATES directories as configured in the settings.py 
                # Django searches for the file in the that directory.

    return HttpResponse( itemTemplate.render())
                # The render method of the template object processes the loaded
                # HTML template and returns a string containing HTMl content

                # This string containg HTML content is wrapped as HttpResponse
                # and passed to browser which will unpack into HTML

                # In further views we will see render() completely.
         # render() method takes two arguments:
         
                # context (optional): A dictionary that contains the 
                # dynamic data to replace placeholders (variables) in the
                # template.

                # request (optional but recommended): The HTTP request 
                # object, which provides additional context to the 
                # template (for things like URL reversing and accessing 
                # user information).

def items(request):


              # Note that we already added data into DB/model using
              # py manage.py shell, 

       items = Item.objects.all().values()       
       # print(items)
              # model_name.objects : Django automatically provides a
              # manager object called .objects for all models. Using 
              # it as a handle/ reference to corresponding model/relation
              # We can query/ modify that model/relation. Note that it
              # is object, dont call it like funcn, use it like this
              # model_name.objects.all()

              #  QuerySet is a collection of database queries in Django.
              #  It represents a set of objects (or rows in a database 
              #  table) that you can retrieve, filter, update, or delete. 

              # .all() : This is queryset method which retrieves all records
              #  from the DB table. If ur table contains a huge no of rows
              #  this can be resource-intensive. Combine it with filters 
              #  or pagination when dealing with large datasets.

              # .values() : Note that all() returns queryset object, which
              # is displayed like this - <QuerySet [<Item: Item object (1)>]>
              # Hence to print the actual values of queryset use .values()

              # Op : <QuerySet [{'id': 1, 'name': 'Yoga Matt', 'price': 700}]>

              # Queryset object can be be used to obtain individual column/field
              # values using . operator, if it has single item.    
              # item1 = Item( name = 'some_name', price = some_price)          
              # item1.name , item2.price etc.

              # If there are mulitple items in QuerySet object, just apply indexing
              # or filtering. First lets use indexing
              # item3 = Item.objects.all()[3]
              # item3.name, item3.price

       # CRUD:

          # newItem = Item(name='Workout shirt', price= 500)
              # This creates new instance of Item model called newItem
              # In DB, this corresponds to a new row, with given
              # column field values name, price. The id will be
              # obviously autoincremented internally.
          # member.save()
              # But note that instance just created is in "pending" state
              # It is not yet attached to Item model itself. .save()
              # saves this instance to the model/relation.

       # Creating Multiple Elements:
              # item1 = Item(name = 'Resistance Bands (Set of 5)' , price = 350)   
              # item2 = Item(name = 'Adjustable Dumbbells (Pair)' , price = 700)     
              # item3 = Item(name = 'Jump Rope (Speed Training)' , price = 200)      
              # item_list = [item1, item2, item3]
              # for x in item_list:
              #     x.save()
       # Update
              # After obtaining individual rows with indexing/filtering, we can 
              # update them as well by saying x.field= val
              # item2 = Item.objects.all()[2]
              # item2.price = 800
              # Dont forget to save item2.save()

       # Deletion
              # Again obtain the row u want to delete.
              # item3 = Item.objects.all()[3]
              # Apply the .delete() on it. No need to save(). It will
              # delete from table entirely
              # item3.delete()
              # Op : (1, {'items.Item': 1})    # denotes 1 item deleted

       # After performing the modifications, apply migrations

       # Now lets load the model data in the views to send it to the
              # template.
       myitems = Item.objects.all().values()
              # Items queryset to be sent
       myTemplate = loader.get_template('items.html')

       context = {
              'myitems' : myitems,
       }
              # context is python dict, containing data to be sent to 
              # the template. Why dict?
              # The template engine expects a mapping of variable 
              # names (keys) to their values. Again Why?
              # The keys in the dictionary become the variable names 
              # accessible in the template.
              # The values are the actual data that will replace those
              # variables during template rendering.

       return HttpResponse( myTemplate.render( context, request))
              # Here Render() processes html template, which involves
              # injecting dynamic data. Hence it needs context.

              # When u provide context/data to the render(), it
              # also uses request object internally. Hence we provide
              # request also.

def item_details( request , id):
              # Note that the "id" parameter here is extracted from url
              # passed by userclick, and sent to this view by the
              # urls.py where while defining urlpatterns, we seperate
              # parameters like id.

              # Now the item correspoding to id requested must be 
              # querried and injected back to template

       requested_Item = Item.objects.get(id = id) 
              # There 2 main methods for filtering/querrying data in django

              # get() : Fetches a single object from the database that matches 
                            # the given filter criteria.
                             
              # filter() : when you want to get all objects that match your
                                   # lookup parameters.
       template = loader.get_template('item_details.html')
       context = {
              'myitem' : requested_Item,
       }
       return HttpResponse( template.render( context, request))

def home(request):
       # Home page of the site
       template = loader.get_template('index.html')
   
       return HttpResponse( template.render())


def test( request ):
       # USed for testing 
       template = loader.get_template('test.html')
       context = {
              'animals': ['tiger', 'monkey','cat','dog']
       }
       return HttpResponse( template.render(context, request))


       




