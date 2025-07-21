from django.contrib import admin

from product.models import Product, Size, Color, Information

# Register your models here.
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Information)