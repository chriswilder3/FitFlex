from django.db import models

from django.core.validators import MinLenthValidator, RegexValidator
# Create your models here.

class User( models.Model):

    name = models.CharField( max_length = 255)
    username = models.CharField( max_length = 255)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField( 
        max_length= 10,
        validators = [
            MinLenthValidator(10),
            RegexValidator(
                regex = r'^\d{10}',
                message = 'Phone no must be exact 10 digits'
            )
        ],
        unique = True
    )

    def __str__(self):
        return f' {self.name} '

