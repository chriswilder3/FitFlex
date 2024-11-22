from django.db import models

from django.core.validators import MinLengthValidator, RegexValidator
# Create your models here.

class User( models.Model):

    name = models.CharField( max_length = 255)
    username = models.CharField( max_length = 255
                , unique = True, null = False)
    email = models.EmailField( null = False)
    address = models.TextField()
    phone = models.CharField( 
        max_length= 10,
        validators = [
            MinLengthValidator(10),
            RegexValidator(
                regex = r'^\d{10}',
                message = 'Phone no must be exact 10 digits'
            )
        ],
        unique = True
    )
    password= models.CharField( max_length = 255,
                                 null = False)

    cart = models.JSONField( null = True)

    orders = models.JSONField( null = True)
    

    def __str__(self):
        return f' {self.name} '

