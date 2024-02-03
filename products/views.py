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

def category_page(request, cat_id):
    categories = Product.objects.filter(Category=cat_id)
    category_name = Prod_Category.objects.filter(pk=cat_id).first()
    return render(request, "products/category.html", {'categories' : categories, 'category_name': category_name})