from django.contrib import admin

# Register your SHOP models here.

from .models import Product,Contact,Order

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
