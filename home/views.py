from django.shortcuts import render, redirect, HttpResponse, Http404
from .models import Product, Cart
from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    context = {'products': products}
    return render(request, 'index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect('login')
        cart = Cart(cart_product=product, user=request.user)
        cart.save()
        messages.success(request, 'item added to cartsucessfully')
    try:
        cart = Cart.objects.get(cart_product=product, user=request.user)
    except:
        cart = {
            'cart_product': False
        }
    print(cart)
    context = {'product': product, 'cart': cart}
    return render(request, 'detail_product.html', context)


@login_required
def cart(request):
    products_on_cart = Cart.objects.filter(user=request.user)
    print(products_on_cart)
    if request.method == "POST":
        cart_item = request.POST.get('cart_item')
        cart_item_to_delete = Cart.objects.get(pk=cart_item)
        print(cart_item_to_delete)
        cart_item_to_delete.delete()
        return redirect('cart')
    context = {'cart_list': products_on_cart}
    return render(request, 'cart.html', context)
