from django.shortcuts import render
from .models import Prod_Category, Product, Order
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    
    return render(request, "products/test_home.html", context)