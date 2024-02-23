from django.shortcuts import get_object_or_404, render, redirect
from .models import Prod_Category, Product, Order
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.

@login_required
def home(request):
    search_query = request.GET.get('search', '').strip()
    products = Product.objects.all().order_by('Category')  
    
    if search_query:
        products = products.filter(Q(Prod_Name__icontains=search_query),Q(Pod_Description__icontains=search_query))
    
    context = {
        'products': products,
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
    messages.success(request, "Successfully Added to cart!")
    return redirect('view_cart')

def remove_from_cart(request, prod_id):
    my_cart = Order.objects.filter(Product_ID=prod_id)
    messages.success(request, f"Successfully deleted {my_cart.first()}!")
    my_cart.delete()
    return redirect('view_cart')

@login_required
def view_cart(request):
    total_price = 0
    my_cart = Order.objects.filter(user=request.user.id)
    print(my_cart)
    for items in my_cart:
        total_price += items.Product_ID.Pod_Price
    return render(request, "products/cart.html", {"my_cart": my_cart, "total_price": total_price})