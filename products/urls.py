from django.urls import path
from .views import home, category_page, add_to_cart, view_cart, remove_from_cart

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:cat_id>/', category_page, name='category'),
    path('<int:prod_id>', add_to_cart, name='cart'),
    path('cart/', view_cart, name='view_cart'),
    path('delete_cart/<int:prod_id>/', remove_from_cart, name='delete_from_cart'),
]
