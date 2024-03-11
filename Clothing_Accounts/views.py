from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from ClothingApp.models import *


def home(request):
    catg = Category.objects.all()

    user = request.user
    if user.is_authenticated:
        length = len(Cart.objects.filter ())
        cart_details = Cart.objects.filter () [:2]
        all_cart = Cart.objects.filter ()
        subtotal = 0

        for i in  all_cart :
            a = (i.product.price) * (i.quantity)
            subtotal += a


    return render(request, 'home.html', locals())


def Registration(request):
     if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get ('email')
        firstname = request.POST.get ('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
       # print("password is", password)
       # print("password is", password1)
        if password == password1:
            if User.objects.filter(Q(username = name) | Q(email = email)).exists():
                messages.warning(request, "Username or Email Already Taken")
            else:
                user = User.objects.create_user(username=name, email=email, first_name=firstname, last_name=lastname, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, "Account Created")
                return redirect('Log_in')
        else:
            messages.warning(request, "Password Not Matched")

     return render(request, 'Accounts/Registration.html')

def Log_in(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user= authenticate(username=name, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are Successfully logged in!")
            return redirect('home')
        else:
            messages.warning(request, "No User Found!")
            return redirect('Registration')



     return render(request, 'Accounts/Log_in.html')

def log_out(request):
    logout(request)
    messages.warning(request, "User Logged Out!")
    return redirect('Log_in')


#logout er kaj done bt cart er ta baki














