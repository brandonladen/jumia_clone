from django.urls import path
from .views import Customer_signUp, Customer_login

urlpatterns = [
    path('signup/', Customer_signUp, name='signup'),
    path('login/', Customer_login, name='login'),
]
