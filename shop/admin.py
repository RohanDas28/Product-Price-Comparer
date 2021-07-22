from django.contrib import admin

from . models import Product
from . models import Contact

admin.site.register(Product)
admin.site.register(Contact)
