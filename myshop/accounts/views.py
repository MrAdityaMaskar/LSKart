from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .managers import CustomUserManager
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            return redirect('login')

            
       
            
    
    return render(request, 'accounts/register.html', {'form':form})


def loginPage(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email," ",password)
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            # User is authenticated
            login(request,user)
            
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
        else:
            messages.info(request, 'Something Went Wrong')
            
        
    return render(request, 'accounts/login.html')

