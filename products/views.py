from django.shortcuts import get_object_or_404, render, redirect
from .models import Prod_Category, Product, Order
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
def add_to_cart(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    Order.objects.create(
        Order_ID = str(uuid.uuid4()), #Generates a random ID
        user = request.user,
        Product_ID = product,
    )
    return messages.success(request, "Successfully Added to cart!")

@login_required
def view_cart(request):
    total_price = 0
    my_cart = Order.objects.filter(user=request.user.id)
    print(my_cart)
    for items in my_cart:
        total_price += items.Product_ID.Pod_Price
    return render(request, "products/cart.html", {"my_cart": my_cart, "total_price": total_price})