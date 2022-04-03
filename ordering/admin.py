from django.contrib import admin

from ordering.models import Collection, Product, Restaurant

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Restaurant)
