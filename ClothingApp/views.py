from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
# Create your views here.

def product(request, id):
    user = request.user
    subcategory = SubCategory.objects.get(id=id)
    category = Category.objects.all()
    length = len(Cart.objects.filter())
    cart_details = Cart.objects.filter()[:2]
    all_cart =Cart.objects.filter()
    subtotal = 0
    for i in all_cart:
        a = i.product.price * i.quantity
        subtotal += a

    prod = PRODUCT.objects.filter(subcategory=subcategory)
    return render(request, 'Shop/all_product.html', locals())


def single_product(request, id):
    user = request.user
    if user.is_authenticated:
        length = len(Cart.objects.filter(user=user))
        cart_details = Cart.objects.filter(user=user)[:2]
        all_cart = Cart.objects.filter(user=user)
        subtotal = 0
        for i in all_cart:
            a = i.product.price * i.quantity
            subtotal += a

        single_product = PRODUCT.objects.get(id=id)

    return render(request, 'Shop/single_product.html', locals())

def addtocart(request, id):
    prod= PRODUCT.objects.get(id=id)
    user = request.user
    if prod:
        if user.is_authenticated:
            try:
                cart = Cart.objects.get (Q(user=user) & Q(product=prod))
                if cart:
                    cart.quantity += 1
                    # print('quantity is',cart.quantity)
                    cart.save()
                    return redirect(request.META['HTTP_REFERER'])
            except:
                    new_cart = Cart.objects.create (user=user,product=prod )
                    new_cart.save()
                    return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('Log_in')
        return redirect(request.META['HTTP_REFERER'])



def remove_cart(request, id):
    remove_cart = Cart.objects.get( id = id )
    remove_cart.delete()

    return redirect(request.META['HTTP_REFERER'])


def cart(request):
    user = request.user
    if user.is_authenticated:
        length = len (Cart.objects.filter(user=user))
        all_cart = Cart.objects.filter(user=user)
        subtotal = 0
        for i in all_cart:
            n= i.product.price * i.quantity
            subtotal += n

    return render(request, 'Shop/shopping_cart.html', locals())


def plus_cart(request, id):
    prod = PRODUCT.objects.get(id=id)
    user = request.user
    if prod:
        if user.is_authenticated:
            cart = Cart.objects.get(user=user, product=prod)
            if cart:
                cart.quantity += 1
                cart.save()
                return redirect(request.META['HTTP_REFERER'])

    return redirect(request.META['HTTP_REFERER'])


def minus_cart(request, id):
    user = request.user
    prod = PRODUCT.objects.get(id=id)
    if user.is_authenticated:
        cart = Cart.objects.get(user=user, product=prod)
        if cart:
            cart.quantity -= 1
            if cart.quantity < 1:
                cart.delete()
                return redirect(request.META['HTTP_REFERER'])
            cart.save()
            return redirect(request.META['HTTP_REFERER'])

    return redirect(request.META['HTTP_REFERER'])




