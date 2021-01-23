from django.contrib import admin

# Register your models here.
from .models import Product, Cart
admin.site.register(Product)
admin.site.register(Cart)