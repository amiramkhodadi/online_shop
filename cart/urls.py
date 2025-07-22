from django.urls import path
from . import views
urlpatterns = [
    path('detail/' , views.CartView.as_view(), name='cart_detail'),
    path('add-to/<int:pk>', views.AddToCartView.as_view(), name='add_to_cart'),

]