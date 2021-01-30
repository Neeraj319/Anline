from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ViewAllProduct, name='SellersHome'),
    path('SellerProductDetail/<int:pk>',
         SellerProductDetail, name='SellerProductDetail'),
    path('AllProducts', ShowAllProducts, name='ShowAllProducts'),
    path('AddProduct', add_product, name='add_product'),
    path('DeleteProduct/<int:pk>', delete_product, name='DeleteProduct'),
    path('EditProduct/<int:pk>', edit_product, name='EditProduct'),
]
