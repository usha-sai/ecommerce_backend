# Example URL configuration (shop/urls.py)
from django.urls import path
from .views import ProductListCreate

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    # Add more URLs as needed
]
