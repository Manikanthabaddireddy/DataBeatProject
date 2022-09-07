from itertools import product
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.views import Product_Report, product
# Create your views here.
def login_user(request):
    
    if request.method=='POST':
        Name = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=Name, password=password)
        if user is not None:
            login(request, user)
            return redirect(Product_Report)
        else:
            messages.success(request,('Hey! You entered invalid Name or Password'))
            return render(request,'login.html')
           
    else:
        return render(request,'register\login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password_2=request.POST['Re_password']
        email=request.POST['email']
        if password==password_2:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            messages.success(request,('Hey! You have sign-up successfully'))
            return redirect('/')
        else:
            messages.success(request,('Hey! you entered wrong credentials or password miss match'))
            return render(request,'register\register.html')
    else:
        return render(request,'register\\register.html')