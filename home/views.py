from django.shortcuts import render, redirect, HttpResponse, Http404
from .models import Product, Cart, ProductImage
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import an_type
from django.core.mail import send_mail
# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {'products': products, 'filters': an_type}
    return render(request, 'index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect('login')
        cart = Cart(cart_product=product, user=request.user)
        cart.save()
        messages.success(request, 'item added to cartsucessfully')
    more_product_images = ProductImage.objects.filter(product=product)
    try:

        cart = Cart.objects.get(cart_product=product, user=request.user)
    except:
        cart = {
            'cart_product': False
        }
    print(cart)
    context = {'product': product, 'cart': cart,
               'more_images': more_product_images}
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


def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        serach_result = Product.objects.filter(name__icontains=query)
        context = {
            'result': serach_result
        }
    if request.method == "POST":
        query = request.POST.get('filter')
        serach_result = Product.objects.filter(product_type__icontains=query)
        context = {
            'result': serach_result
        }
    return render(request, 'search.html', context)


def buy_product(request, pk):
    product = Product.objects.get(pk=pk)
    user_email = request.user.email
    if request.method == "POST":
        send_mail('order came', 'somebody wants to buy' + product.name, user_email,  [
                  'itskop520@gmail.com'])
        messages.success(request, 'item buyed sucessflly')
    context = {
        'product': product
    }
    return render(request, 'buy.html', context)
