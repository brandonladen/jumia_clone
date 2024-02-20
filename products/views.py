from django.shortcuts import get_object_or_404, render
from .models import Prod_Category, Product, Order
from operator import attrgetter
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    products_all = Product.objects.all()
    products = Product.objects.all().order_by('Category')
    context = {
        'products': products,
        'products_all' : products_all,
    }
    
    return render(request, "products/index.html", context)

@login_required
def category_page(request, cat_id):
    categories = Product.objects.filter(Category=cat_id)
    category_name = Prod_Category.objects.filter(pk=cat_id).first()
    return render(request, "products/category.html", {'categories' : categories, 'category_name': category_name})

@login_required
def cart_page(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    context = {
        'product' : product,
    }
    return render(request, 'products/cart.html', context)