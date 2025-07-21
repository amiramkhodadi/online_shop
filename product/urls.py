from django.urls import path
from . import  views
urlpatterns = [
    # path('list/', views.ProductListView.as_view(), name='product-list'),
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]