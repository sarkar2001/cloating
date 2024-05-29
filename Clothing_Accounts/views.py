from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from ClothingApp.models import *
from .models import *
from django.core.paginator import Paginator



def home(request):
    category = Category.objects.all()
    slides = SliderBanner.objects.all()
    products = PRODUCT.objects.all()
    brands = Brand.objects.all()

    user = request.user
    if user.is_authenticated:
        length = len(Cart.objects.filter(user=user))
        cart_details = Cart.objects.filter(user=user)[:2]
        all_cart = Cart.objects.filter(user=user)
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
        
        if user and user.is_staff:
            login(request,user)
            messages.success(request, "You are Successfully logged in!")
            return redirect('authority:authority_admin')
        
        elif user:
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
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Fix the typo in the model name from UserMassage to UserMessage
            obj = UserMessage.objects.create(user=user,
                                             name=name,
                                             email=email,
                                             subject=subject,
                                             message=message,
                                             )
            obj.save()
            messages.success(request, 'Message sent successfully')  # Display success message
            # Redirect to the same page after form submission
            return redirect(request.META.get('HTTP_REFERER'))

    # Move context creation outside the authentication block
    context = {
        'contact_us': contact_us,
    }
    return render(request, 'contact.html', context)


def allpro(request):
    products = PRODUCT.objects.all()
    paginator = Paginator(products, 3)
    # page_list= request.GET.get('search')
    page_number = request.GET.get('page', 1)
    products = paginator.get_page(page_number)
    search_query= request.GET.get('search')
    if search_query:
        products = PRODUCT.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        # print('search_query')
        context = {
            'all_product': products
        }
    return render(request, 'Shop/allpro.html', locals())

