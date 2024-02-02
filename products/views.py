from django.shortcuts import render
from .models import Prod_Category, Product, Order
from operator import attrgetter
# Create your views here.

def home(request):
    products_all = Product.objects.all()
    products = Product.objects.all().order_by('Category')
    context = {
        'products': products,
        'products_all' : products_all,
    }
    
    return render(request, "products/index.html", context)