from django.db import models
from django.contrib.auth.models import User
from Auth_users.models import Buyer
an_type = (
    ('Electronics', 'Electronics'),
    ('Furniture', 'Furniture'),
    ('Food', 'Food'),
    ('Gaming', "Gaming"),
    ('Toys', 'Toys'),
    ('Clothing', 'Clothing'),
    ('Vehicle', 'Vehicle')
)
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(null=True,
                                  blank=True,
                                  upload_to='product_images')
    price = models.FloatField()

    product_type = models.CharField(max_length=50, choices=an_type)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.cart_product.name


class ProductImage(models.Model):
    '''
    this model is for extra images for the product
    '''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pictures = models.ImageField(
        upload_to='product_images', blank=True)

    def __str__(self):
        return self.product.name
