from django.shortcuts import render
from django.views import View


# Create your views here.
class CartView(View):
    def get(self, request):
        return render(request , "cart/cart_detail.html" ,{})