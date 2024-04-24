from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from ClothingApp.models import *
from .models import *


def home(request):
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    subsubcategory = Subsubcategory.objects.all()
    slides = SliderBanner.objects.all()
    products = PRODUCT.objects.all()
    brands = Brand.objects.all()

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


def aboutus(request):
    about= AboutUs.objects.all()
    context = {
        'about' : about,
    }
    return render(request, 'aboutus.html', context)



def contact(request):
    user = request.user
    contact_us = ContactUs.objects.all()
    if user.is_authenticated:
        if request.method == 'POST' or request.method == 'post':
            user = user
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            massage = request.POST.get('massage')

            obj = UserMassage.objects.create(user=user,
                                             name=name,
                                             email=email,
                                             subject=subject,
                                             massage=massage,
                                             )
            obj.save()
            messages.success(request, f'Successfully Done')
            return redirect(request.META.get('HTTP_REFERER'))
        context = {
            'contact_us': contact_us,
        }
    return render(request, 'contact.html', locals())






def Base(request):
    products = PRODUCT.objects.all()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    subsubcategory = Subsubcategory.objects.all()

    if request.method == 'GET':
        src = request.GET.get('search')
        print(src)
        if src:
            products = PRODUCT.objects.filter(title__icontains=src)
            subcategory = SubCategory.objects.filter(Q(name__icontains=src) | Q(category__icontains=src))
            subsubcategory = Subsubcategory.objects.filter(Q(name__icontains=src) | Q(subcategory__icontains=src))
        else:
            products = PRODUCT.objects.all()
            subcategory = SubCategory.objects.all()
            subsubcategory = Subsubcategory.objects.all()

    return render(request, 'base.html', locals())

