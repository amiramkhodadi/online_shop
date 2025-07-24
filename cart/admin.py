from django.contrib import admin
from . models import Order , OrderItem



class OrderItemsAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ('user' , 'is_paid')
   inlines = (OrderItemsAdmin, )
   list_filter = ('is_paid' , )




