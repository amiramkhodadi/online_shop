from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request , "cart/cart_detail.html" ,{})


class AddToCartView(View):
    def post(self ,request):
        return redirect('cart_detail')