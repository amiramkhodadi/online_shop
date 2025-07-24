from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .cart_module import Cart
from product.models import Product


# Create your views here.
class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request , "cart/cart_detail.html" ,{'cart': cart})


class AddToCartView(View):
    def post(self ,request , pk ):
        product = get_object_or_404(Product, pk=pk)
        quantity = request.POST['quantity']
        size = request.POST.get('size', '-')
        color = request.POST.get('color', '-')
        cart = Cart(request)
        cart.add_to_cart(product ,quantity, color , size)
        return redirect('cart_detail')

class RemoveFromCartView(View):
    def get(self , request , id ):
        cart = Cart(request)
        cart.delete_cart(id)
        return redirect('cart_detail')
