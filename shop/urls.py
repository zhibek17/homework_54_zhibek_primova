from django.urls import path
from .views import *

urlpatterns = [
    path('', products_view, name='products_view'),
    path('products/', products_view, name='products_view'),
    path('products/<int:product_id>/', product_view, name='product_view'),
    path('categories/add', category_add_view, name='category_add_view'),
    path('products/add', product_add_view, name='product_add_view'),
]
