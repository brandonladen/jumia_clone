from django.urls import path
from .views import Customer_signUp, Customer_login, profile, logout, update_profile

urlpatterns = [
    path('signup/', Customer_signUp, name='signup'),
    path('login/', Customer_login, name='login'),
    path('login/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('update_profile/<int:c_id>/', update_profile, name='update_profile'),
]
