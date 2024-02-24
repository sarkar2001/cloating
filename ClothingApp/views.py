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

def AddtoCart(request, id):
    prod= PRODUCT.objects.get(id=id)
    user = request.user
    if prod:
        if user.is_authenticated:
            try:
                cart = Cart.objects.get (Q(user=user) & Q(product=prod))
                if cart:
                    cart.quantity += 1
                    cart.save()
                    return redirect(request.META['HTTP_REFERER'])
            except:
                    new_cart = Cart.objects.create (user=user,product=prod )
                    new_cart.save()
                    return redirect(request.META['HTTP_REFERER'])


        else:
            return redirect('Log_in')
        return redirect(request.META['HTTP_REFERER'])







