from django.contrib import admin
from iteminfo.models import Item, Warehouse, Assignment

admin.site.register(Item)
admin.site.register(Assignment)
admin.site.register(Warehouse)
