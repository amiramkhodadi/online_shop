from django.shortcuts import render
from django.views.generic import DetailView

from product.models import Product
from django.views.generic.list import ListView


# Create your views here.
# class ProductListView(ListView):
#     model = Product
#     template_name = 'product/product_detail.html'
#     context_object_name = 'products'
#     paginate_by = 1
#


class ProductDetailView(DetailView):
    model = Product

