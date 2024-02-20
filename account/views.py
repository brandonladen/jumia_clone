from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerCreationForm, CustomerLoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def Customer_signUp(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomerCreationForm()
        
    context = {
        'form': form
    }
    return render(request, "account/CustomerCreationForm.html", context)
        

def Customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomerLoginForm()
    return render(request, 'account/CustomerLoginForm.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'account/profile.html')