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

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/products_list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        colors = self.request.GET.getlist('color')
        sizes = self.request.GET.getlist('size')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        context =super(ProductListView, self).get_context_data()
        print(colors, sizes, min_price, max_price)
        queryset = Product.objects.all()
        if colors :
            queryset = queryset.filter(color__title__in=colors)
        if sizes :
            queryset = queryset.filter(size__title__in=sizes)
        if min_price and max_price :
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        context['products'] = queryset
        return context
