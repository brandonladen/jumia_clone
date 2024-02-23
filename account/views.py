from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerCreationForm, CustomerLoginForm, CustomerUpdateProfile
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


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
    return redirect(reverse('login'))
    #return redirect('login')

@login_required
def profile(request):
    return render(request, 'account/profile.html')

@login_required
def update_profile(request, c_id):
    cust = get_object_or_404(User, pk=c_id)
    print(cust)
    form = CustomerUpdateProfile(request.POST or None, instance=cust)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Updated your profile!")
        return redirect('profile')
    else:
        form = CustomerUpdateProfile(instance=cust)
        
    context = {
        'form':form,
    }
    return render(request, 'account/profile_update.html', context)