from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('cart', cart, name='cart'),
]