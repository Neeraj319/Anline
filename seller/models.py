from django.db import models
from home.models import Product
# Create your models here.
from django.contrib.auth.models import User
from Auth_users.models import Buyer


class ProductsToDeliver(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductPackaged = models.BooleanField(default=False)
    ProductShipeed = models.BooleanField(default=False)
    ProductDilivered = models.BooleanField(default=False)
    ProductDeliveryDate = models.DateField(auto_now_add=False)

    def __str__(self):
        return f'{self.product}'
