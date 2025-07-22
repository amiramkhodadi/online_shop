from itertools import product

from product.models import Product

CART_SESSION_ID = 'cart'
class Cart:
    def __init__(self ,request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            my_product = Product.objects.get(id=item['id'])
            item["product"] = my_product
            item['total'] = my_product.price * item["quantity"]
            yield item

    def unique_id_generator(self, product_id, size, color):
        size = size or '-'
        color = color or '-'
        return f'{product_id}-{size}-{color}'

    def add_to_cart(self, product ,  quantity , color , size ):
        unique = self.unique_id_generator(product_id=product.id , size=size, color=color)
        if unique not in self.cart:
            self.cart[unique] = {
                'quantity': int(quantity),
                'price': str(product.price),
                'size': size,
                'color': color,
                'id': product.id
            }
        else:
            self.cart[unique]['quantity'] += int(quantity)
        self.save()

    # def delete_cart(self):
