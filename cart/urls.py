from django.urls import path
from . import views
urlpatterns = [
    path('detail/' , views.CartView.as_view(), name='cart_detail'),
    path('add-to/<int:pk>', views.AddToCartView.as_view(), name='add_to_cart'),
    path('del-to/<str:id>', views.RemoveFromCartView.as_view(), name='del_to_cart'),
    path('cr-order/', views.CreateOrderView.as_view(), name='create_order'),
    path('order-detail/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('order-descount/<int:pk>', views.OrderDescountView.as_view(), name='apply_coupon'),

]