from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pricture = models.ImageField(null=True,
                                 blank=True,
                                 upload_to='product_images')
    price = models.FloatField()
    an_type = (
        ('Electronics', 'Electronics'),
        ('Furniture', 'Furniture'),
        ('Food', 'Food'),
        ('Gaming', "Gaming"),
        ('Toys', 'Toys'),
        ('Clothing', 'Clothing'),
        ('Vehicle', 'Vehicle')
    )
    product_type = models.CharField(max_length=50, choices=an_type)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.cart_product.name
