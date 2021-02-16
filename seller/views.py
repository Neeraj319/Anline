from django.shortcuts import render, redirect
import os
from .models import ProductsToDeliver
from Auth_users.models import Buyer
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from home.models import Product
# Create your views here.
from django.contrib import messages
from home.models import an_type, ProductImage
from home.models import ProductImage


@login_required
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

    return render(request, 'home.html', context)


@login_required
def SellerProductDetail(request, pk):
    try:
        if request.user.buyer:
            return redirect('home')
    except:
        product_details = ProductsToDeliver.objects.get(pk=pk)
        a = Buyer.objects.get(pk=product_details.user.pk)
        extra_charge = 50.50 + product_details.product.price
        buyers_email = a.user.email
        address = a.user.buyer.address
        if request.method == 'POST':
            value_of_Product_Packaged = request.POST.get('Product_Packaged')
            value_of_Product_Shipeed = request.POST.get('Product_Shipeed')
            value_of_Product_Dilivered = request.POST.get('Product_Dilivered')
            if value_of_Product_Packaged:
                product_details.ProductPackaged = True
                product_details.save()
                send_mail('your order has been packed', 'dear coustomer your order has been packed ' + product_details.product.name, 'itskop520@gmail.com',  [
                    buyers_email])
                return redirect('SellersHome')
            elif value_of_Product_Shipeed:
                product_details.ProductShipeed = True
                product_details.save()
                send_mail('your order has been shipped', 'dear coustomer your order has been shipped ' + product_details.product.name, 'itskop520@gmail.com',  [
                    buyers_email])
                return redirect('SellersHome')
            elif value_of_Product_Dilivered:
                product_details.ProductDilivered = True
                product_details.save()
                send_mail('your order has been delivered', 'dear coustomer your order has been delivered ' + product_details.product.name, 'itskop520@gmail.com',  [
                    buyers_email])
                return redirect('SellersHome')
        context = {
            'product_details': product_details,
            'address': address,
            'extra_charge': extra_charge
        }
    return render(request, 'SellerProduct.html', context)


@login_required
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


@login_required
def add_product(request):
    try:
        if request.user.buyer:
            return redirect('home')
    except:
        context = {
            'filters': an_type

        }
        if request.method == "POST":
            name = request.POST.get('ProductName')
            price = request.POST.get('ProductPrice')
            ProductDescription = request.POST.get('ProductDescription')
            img = request.FILES.get('img')
            img1 = request.FILES.get("img1")
            img2 = request.FILES.get('img2')
            img3 = request.FILES.get('img3')
            query = request.POST.get('ProductCategory')
            print(name, price, ProductDescription, img, query)
            product = Product.objects.create(
                name=name, description=ProductDescription, price=float(price), thumbnail=img, product_type=query)
            product.save()
            if img1 is not None:
                print('first img')
                ProductImage.objects.create(product=product, pictures=img1)
            else:
                pass
            if img2 is not None:
                print('2nd img')
                ProductImage.objects.create(product=product, pictures=img2)
            else:
                pass
            if img3 is not None:
                print('3rd img')
                ProductImage.objects.create(product=product, pictures=img3)
            else:
                pass
            messages.success(request, 'item created sucessfully')
            return redirect('ShowAllProducts')

    return render(request, 'add_product.html', context)


@login_required
def delete_product(request, pk):
    try:
        if request.user.buyer:
            return redirect('home')
    except:
        product = Product.objects.get(pk=pk)
        product_images = ProductImage.objects.filter(product=product)
        if request.method == "POST":
            if product_images is not None:
                for i in product_images:
                    os.remove('media/' + str(i.pictures))
                    print('deleted')
            os.remove('media/' + str(product.thumbnail))
            product.delete()
            messages.success(request, 'item deleted sucessfully')
            return redirect('ShowAllProducts')
        context = {
            'product': product
        }
        return render(request, 'delete_product.html', context)


@login_required
def edit_product(request, pk):
    try:
        if request.user.buyer:
            return redirect('home')
    except:
        product = product = Product.objects.get(pk=pk)
        if request.method == "POST":
            name = request.POST.get('ProductName')
            price = request.POST.get('ProductPrice')
            ProductDescription = request.POST.get('ProductDescription')
            img = request.FILES.get('img')
            print(name, price, ProductDescription, img)
            product.name = name
            product.price = float(price)
            product.description = ProductDescription
            if img:
                product.thumbnail = img
            product.save()
            return redirect('ShowAllProducts')
        context = {
            'product': product,
            'filters': an_type
        }
    return render(request, 'edit_product.html', context)
