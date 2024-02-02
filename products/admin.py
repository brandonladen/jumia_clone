from django.contrib import admin
from .models import Product, Prod_Category, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Prod_Category)
admin.site.register(Order)