from django.shortcuts import render, redirect, HttpResponse, Http404
from .models import Product, Cart
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        cart = Cart(cart_product=product, user=request.user)
        cart.save()
        messages.success(request, 'item added to cartsucessfully')
    context = {'product': product}
    return render(request, 'detail_product.html', context)


def cart(request):
    products_on_cart = Cart.objects.filter(user=request.user)
    print(products_on_cart)
    context = {'cart_list': products_on_cart}
    return render(request, 'cart.html', context)
