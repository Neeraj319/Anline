from django.db import models
from home.models import Product
# Create your models here.


class ProductsToDeliver(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductPackaged = models.BooleanField(default=False)
    ProductShipeed = models.BooleanField(default=False)
    ProductDilivered = models.BooleanField(default=False)
