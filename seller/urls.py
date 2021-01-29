from django.urls import path, include
from .views import *
urlpatterns = [
    path('', ViewAllProduct, name='SellersHome'),
    path('SellerProductDetail/<int:pk>',
         SellerProductDetail, name='SellerProductDetail'),
    path('AllProducts', ShowAllProducts, name='ShowAllProducts'),

]
