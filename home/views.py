from django.shortcuts import render, redirect, HttpResponse, Http404 , HttpResponseRedirect
from .models import Product, Cart, ProductImage
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import an_type
from Auth_users.models import Buyer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.core.mail import send_mail
from seller.models import ProductsToDeliver
from product_review.models import PorductReview
# Create your views here.


def home(request):
    # print(request.META.get('HTTP_REFERER') , 'helllo')
    try:
        if request.user.seller:
            return redirect('SellersHome')
    except:
        products = Product.objects.all()
        context = {'products': products, 'filters': an_type}
    return render(request, 'index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    product_review = PorductReview.objects.filter(product=product)
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect('login')
        cart = Cart(cart_product=product, user=request.user.buyer)
        cart.save()
        messages.success(request, 'item added to cartsucessfully')

    more_product_images = ProductImage.objects.filter(product=product)
    more_products = Product.objects.filter(product_type=product.product_type)
    print(more_products)
    try:

        cart = Cart.objects.get(cart_product=product, user=request.user.buyer)
    except:
        cart = {
            'cart_product': False

        }
    print(cart)
    context = {'product': product, 'cart': cart,
               'more_images': more_product_images,
               'more_products': more_products[0:3],
               'product_review' : product_review
               }
    return render(request, 'detail_product.html', context)


@login_required
def cart(request):
    try:
        if request.user.seller:
            return redirect('SellersHome')
    except:
        products_on_cart = Cart.objects.filter(user=request.user.buyer)
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
        search_query = request.GET.get('search-query')
        serach_result = Product.objects.filter(product_type__icontains=query)
        normal_serach = serach_result.filter(name__icontains=search_query)
        context = {
            'result': normal_serach,
            'query': query
        }

    return render(request, 'search.html', context)


@login_required
def buy_product(request, pk):
    try:
        if request.user.seller:
            return redirect('SellersHome')
    except:
        product = Product.objects.get(pk=pk)
        user_email = request.user.email
        if request.method == "POST":
            ProductsToDeliver.objects.create(
                product=product, user=request.user.buyer)
            send_mail('order came from ' + str(request.user.buyer), 'an order from ' + str(request.user.buyer) + 'has come' + product.name + '\nproduct url - http://127.0.0.1:8000/detail/' + str(product.pk), user_email,  [
                'itskop520@gmail.com'])

            messages.success(request, 'item order sucessflly')
            return redirect('buy', product.pk)
        extra_charge = 50.50 + product.price
        context = {
            'product': product,
            'charge': extra_charge
        }
    return render(request, 'buy.html', context)


@login_required
def User_Ordered_Product(request):

    try:
        if request.user.buyer:
            Product = ProductsToDeliver.objects.filter(user=request.user.buyer)
            context = {
                'Product': Product
            }

    except:
        return redirect('SellersHome')
    return render(request, 'user_products_to_buy.html', context)


@login_required
def profile(request, user_name):
    buyer = Buyer.objects.get(user = request.user)
    if buyer == request.user.buyer:
        if request.method =="POST":
            address = request.POST.get('address')
            phone = request.POST.get("phone")
            if (address or phone) == '':
                messages.error(request , 'fileds cant be empty')
                return redirect('profile' , request.user.buyer)
            else:
                buyer.phone = phone
                buyer.address = address
                buyer.save()
                messages.success(request , 'changes saved sucessfully')
                return redirect('profile' , request.user.buyer)

        context = {
            'profle' : buyer
        }
    else:
        return redirect('home')
    return render(request , 'profile.html' , context)
@login_required
def product_review(request , pk):
    if request.method == "POST":
        review = request.POST.get('review')
        product = Product.objects.get(pk =pk)
        PorductReview.objects.create(user = request.user.buyer , product = product , review = review)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'product' : product
    }
    return render(request , 'detail_product.html' , context)