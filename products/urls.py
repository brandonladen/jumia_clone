from django.urls import path
from .views import home, category_page, cart_page

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:cat_id>/', category_page, name='category'),
    path('cart/<int:prod_id>', cart_page, name='cart'),
]
