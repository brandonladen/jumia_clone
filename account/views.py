from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerCreationForm

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
    pass