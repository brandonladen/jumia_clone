from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerCreationForm, CustomerLoginForm


# Create your views here.
def Customer_signUp(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = CustomerCreationForm()
        
    context = {
        'form': form
    }
    return render(request, "")
        

def Customer_login(request):
    if request.method == "POST":
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           password2= form.cleaned_data['password2']
           user = authenticate(request,username=username,password2=password2)
           if user is not None:
               login(request,user)
               messages.success(request,'succss')