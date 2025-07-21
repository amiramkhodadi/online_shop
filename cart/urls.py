from django.urls import path
from . import views
urlpatterns = [
    path('detail/' , views.CartView.as_view(), name='cart_detail'),

]