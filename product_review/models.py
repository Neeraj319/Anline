from django.db import models

# Create your models here.
from home.models import Product
from Auth_users.models import Buyer
class PorductReview(models.Model):
    user = models.ForeignKey(Buyer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return str(self.user)
    