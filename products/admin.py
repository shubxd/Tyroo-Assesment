from django.contrib import admin
from products.models import Brand, Categories, Product
# Register your models here.

admin.site.register(Brand)
admin.site.register(Categories)
admin.site.register(Product)
