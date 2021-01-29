from django.shortcuts import render, redirect
from .models import ProductsToDeliver
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from home.models import Product
# Create your views here.
from home.models import an_type


def ViewAllProduct(request):
    Product = ProductsToDeliver.objects.filter(ProductDilivered=False)

    try:
        if request.user.buyer:
            print(request.user.buyer)
            return redirect('home')
    except:
        context = {
            'Product': Product
        }
        print('hi')
    return render(request, 'home.html', context)


@login_required
def SellerProductDetail(request, pk):
    try:
        if request.user.buyer:
            return redirect('home')
    except:
        product_details = ProductsToDeliver.objects.get(pk=pk)

        if request.method == 'POST':
            value_of_Product_Packaged = request.POST.get('Product_Packaged')
            value_of_Product_Shipeed = request.POST.get('Product_Shipeed')
            value_of_Product_Dilivered = request.POST.get('Product_Dilivered')
            if value_of_Product_Packaged:
                product_details.ProductPackaged = True
                product_details.save()
                send_mail('your order has been pacaked', 'dear coustomer your order has been packed ' + product_details.product.name, 'itskop520@gmail.com',  [
                    product_details.user.email])
                return redirect('SellersHome')
            elif value_of_Product_Shipeed:
                product_details.ProductShipeed = True
                product_details.save()
                send_mail('your order has been shipped', 'dear coustomer your order has been shipped ' + product_details.product.name, 'itskop520@gmail.com',  [
                    product_details.user.email])
                return redirect('SellersHome')
            elif value_of_Product_Dilivered:
                product_details.ProductDilivered = True
                product_details.save()
                send_mail('your order has been delivered', 'dear coustomer your order has been delivered ' + product_details.product.name, 'itskop520@gmail.com',  [
                    product_details.user.email])
                return redirect('SellersHome')
        context = {
            'product_details': product_details
        }
    return render(request, 'SellerProduct.html', context)


def ShowAllProducts(request):
    try:
        if request.user.buyer:
            return redirect('home')
    except:
        product = Product.objects.all()
        context = {
            'products': product,
            'filters': an_type

        }
    return render(request, 'AllProducts.html', context)
