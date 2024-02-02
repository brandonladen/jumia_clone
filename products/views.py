from django.shortcuts import render
from .models import Prod_Category, Product, Order
from operator import attrgetter
# Create your views here.

def home(request):
    products = Product.objects.all().order_by('Category')
    context = {
        'products': products
    }
    
    return render(request, "products/index.html", context)