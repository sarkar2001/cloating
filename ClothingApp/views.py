from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
# Create your views here.

def product(request, id):
    prod = PRODUCT.objects.filter(category=id)
    return render(request, 'Shop/all_product.html', locals())


def single_product(request, id):
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
        len_cart = len(CART.objects.filter(user=user,purchased=False))
        cart_details = CART.objects.filter(user=user,purchased=False)[:2]
        all_cart = CART.objects.filter(user=user,purchased=False)
        subtotal = 0
        for i in all_cart:
            a = i.product.price * i.quantity
            subtotal += a

    return render(request, 'shop/shopping-cart.html', locals())


def checkout(request):
    user = request.user
    len_cart = len(CART.objects.filter(user=user,purchased=False))
    cart_details = CART.objects.filter(user=user,purchased=False)[:2]
    all_cart = CART.objects.filter(user=user,purchased=False)
    subtotal = 0
    for i in all_cart:
        a = i.product.price * i.quantity
        subtotal += a
    total = subtotal
    try:
        if all_cart:
            for i in all_cart:
                if i.quantity > 1:
                    delivery_charge = 0
                    total += delivery_charge

                elif len_cart > 1:
                    delivery_charge = 0
                    total += delivery_charge
                else:
                    if request.method == 'POST':
                        del_cost = request.POST['deliver']

                        if del_cost == '1':
                            delivery_charge = 70
                            total += delivery_charge
                        else:
                            delivery_charge = 100
                            total += delivery_charge
    except:
        messages.warning(request, "Choose delivery option!")
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'shop/checkout.html', locals())


def plus_cart(request, id):
    prod = PRODUCT.objects.get(id=id)
    user = request.user
    if prod:
        if user.is_authenticated:
            cart = CART.objects.get(user=user, product=prod,purchased=False)
            if cart:
                cart.quantity += 1
                cart.save()
                return redirect(request.META['HTTP_REFERER'])

    return redirect(request.META['HTTP_REFERER'])


def minus_cart(request, id):
    user = request.user
    prod = PRODUCT.objects.get(id=id)
    if user.is_authenticated:
        cart = CART.objects.get(user=user, product=prod,purchased=False)
        if cart:
            cart.quantity -= 1
            if cart.quantity < 1:
                cart.delete()
                return redirect(request.META['HTTP_REFERER'])
            cart.save()
            return redirect(request.META['HTTP_REFERER'])

    return redirect(request.META['HTTP_REFERER'])




