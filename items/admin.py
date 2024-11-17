from django.contrib import admin

from .models import Item
# Register your models here.

class ItemAdmin( admin.ModelAdmin):
    # ItemAdmin is a subclass of admin.ModelAdmin, which provides
    # options for customizing the behavior and appearance of the admin 
    # interface for the Item model.
    
    list_display = ("name", "price",)
    # This defines the columns that will be displayed in the admin list
    # view for the Member model.

admin.site.register(Item, ItemAdmin)