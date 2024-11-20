from django.db import models
            # this module provides classes and methods used
            # to define database models.


# IMP : Django follows ORM

class Item(models.Model):

            # Defines a class Item that inherits from another class 
            # called Model from models module. 
            # By doing this Item became a Django model, based on which
            # django will create a corresponding table of same
            # name, item (lowercased) in the DB.
        
        # As beginner, We will have a name, price for each item. But note
        # that Django will automatically create primary key field 'id'.

        name = models.CharField( max_length = 255)
            # Here name is a model field which represents a column in DB
            # models.CharField() is a field for storing char based data.
            # Note that max_length is required for CharField()

        price = models.DecimalField(max_digits=10, decimal_places=2) 

        description = models.TextField()
        
        category = models.CharField( max_length = 255)

        sub_category = models.CharField( max_length = 255, blank= True)

        item_type = models.CharField( max_length = 255)

        image = models.ImageField( blank= True)

        def __str__(self):
            # When you display a Model as a list, Django displays each 
            # record Member object (1), Member object (2) etc
            # in admin tool.
            # Hence we need to set what to display when we print a
            # model through __str__
            return f' {self.name} '
            # But better is to change How fields will be displayed in 
            # admin tool, using list_display property in admin.py
            # through MemberAdmin class

# IMP Note :

# The name of the table will be derived from the appname & class name,
# converted to lowercase (e.g., item for the Item model). override this
# behavior by specifying the db_table option inside the model’s Meta class


# To apply the model and create the actual table in the database, you 
# need to run migrations. When you add a new model or modify existing 
# models, Django generates migration files to reflect these changes in
# the database schema.

# First, run: python manage.py makemigrations to generate migration
#  files.
# Then, apply the migrations with: python manage.py migrate

# The model can be queried and manipulated using Django’s ORM 
# (Object-Relational Mapping) in the views

