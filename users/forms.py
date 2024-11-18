from django import forms 
        # forms is a Django package that contains Form class.

    
# We know that HTML has forms, But provide more security, management toit
# We rely on Django. In addition, since Django is the backend, through
# GET/POST methods, we have to submit form data to a url (action attr) 
# which is served to to endpoint of a url patterns and a view corrsponding
# to it will handle this form data.

# Form class :
        #  Similar to how Django model describes the logical structure of
        #  an object correspondong to a relation in DB.
        # Form class describes a form and determines how it works & appears.

# In a similar way that a model class’s fields map to database fields, 
# a form class’s fields map to HTML form <input> elements. 

# ( In particular A ModelForm maps a model class’s fields to HTML form 
# <input> elements via a Form)

class SignUpForm( forms.Form):
    name = forms.CharField( label = 'Enter your name', max_length=100)

    # This defines a Form class with a single field (your_name). 
    # The given label to the field, will appear in the <label> when it’s 
    # rendered (other wise It will automatically generate a label for us).

    # A Form instance has an is_valid() method, which runs validation 
    # routines for all its fields. When this method is called, if all 
    # fields contain valid data, it will: return True
    # and then place the form’s data in its cleaned_data attribute.

    # All the forms must be instantiated in the view corresponding to 
    # that forms page. 
    # Then the Form data sent back to a Django website is
    # processed by that view. 