from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('cart', cart, name='cart'),
    path('search', search, name='search'),
    path('buy/<int:pk>', buy_product, name='buy'),
    path('myorders', User_Ordered_Product, name='myorders'),
    path('profile/<str:user_name>' , profile , name = 'profile')
]
