from django.db import models

from account.models import User
from product.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='orders')
    total_price  = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.full_name}  - {self.is_paid}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='items')
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()



    def __str__(self):
        return f'{self.product.title} - {self.color} - {self.size} - {self.price}'



class DiscountCode(models.Model):
    name = models.CharField(max_length=100)
    discount_code = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    def __str__(self):

        return self.name
