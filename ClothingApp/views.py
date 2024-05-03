from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def product(request, id):
    user = request.user
    subcategory = SubCategory.objects.get(id=id)
    category = Category.objects.all()
    length = len(Cart.objects.filter(user=user))
    cart_details = Cart.objects.filter(user=user)[:2]
    all_cart = Cart.objects.filter(user=user)
    subtotal = 0
    for i in all_cart:
        a = i.product.price * i.quantity
        subtotal += a

    prod = PRODUCT.objects.filter(subcategory=subcategory)
    return render(request, 'Shop/all_product.html', locals())


def single_product(request, id):
    user = request.user
    products = PRODUCT.objects.all()
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
    variation = Variation.objects.all()
    user = request.user
    if prod:
        if user.is_authenticated:
            try:
                cart = Cart.objects.get (Q(user=user) & Q(product=prod))
                if cart:
                    quantity = request.POST.get('quantity')
                    # size = request.POST.get('size')
                    # color = request.POST.get('color')
                    cart.quantity += int(quantity)
                    # cart.color = colors
                    # cart.size = sizes
                    # print('quantity is',cart.quantity)
                    cart.save()
                    return redirect(request.META['HTTP_REFERER'])
            except:
                    new_cart = Cart.objects.create (user=user,product=prod)
                    new_cart.save()
                    return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('Log_in')
        return redirect(request.META['HTTP_REFERER'])



def remove_cart(request, id):
    remove_cart = Cart.objects.get( id = id)
    remove_cart.delete()
    return redirect(request.META['HTTP_REFERER'])


def cart(request):
    user = request.user
    products = PRODUCT.objects.all()
    if user.is_authenticated:
        length = len(Cart.objects.filter(user=user))
        cart_details = Cart.objects.filter(user=user)[:2]
        all_cart = Cart.objects.filter(user=user)
        subtotal = 0
        for i in all_cart:
            a = i.product.price * i.quantity
            subtotal += a

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



def brand(request,id):
    return render(request, 'Shop/branding_page.html', locals())


def checkout(request):
    user = request.user
    length = len(Cart.objects.filter(user=user))
    cart_details = Cart.objects.filter(user=user)[:2]
    all_cart = Cart.objects.filter(user=user)
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

                elif  length > 1:
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

    return render(request, 'Shop/checkout.html', locals())


def sslcommerz(request):
    user = request.user
    length = len(Cart.objects.filter(user=user))
    cart_details = Cart.objects.filter(user=user)[:2]
    all_cart = Cart.objects.filter(user=user)
    subtotal = 0
    for i in all_cart:
        a = i.product.price * i.quantity
        subtotal += a
    total = subtotal
    if request.method == 'POST':
        del_cost = request.POST['deliver']

        if del_cost == '2':

            sslcz = SSLCOMMERZ({'store_id': 'niyam6412dc52e1e89', 'store_pass': 'niyam6412dc52e1e89@ssl', 'issandbox': True})
            data = {
                'total_amount': total,
                'currency': "BDT",
                'tran_id': "tran_12345",
                'success_url': "http://127.0.0.1:8020/ClothingApp/success/",
                # if transaction is succesful, user will be redirected here
                'fail_url': "http://127.0.0.1:8020/ClothingApp/fail/",  # if transaction is failed, user will be redirected here
                # 'cancel_url': "http://127.0.0.1:8000/payment-cancelled",
                # after user cancels the transaction, will be redirected here
                'emi_option': "0",
                'cus_name': "test",
                'cus_email': "test@test.com",
                'cus_phone': "01700000000",
                'cus_add1': "customer address",
                'cus_city': "Dhaka",
                'cus_country': "Bangladesh",
                'shipping_method': "NO",
                'multi_card_name': "",
                'num_of_item': 1,
                'product_name': "Test",
                'product_category': "Test Category",
                'product_profile': "general",
            }
            response = sslcz.createSession(data)
            return redirect(response['GatewayPageURL'])
        else:
            return render(request, 'Shop/success.html')

@csrf_exempt
def success(request):
    cart = Cart.objects.filter()
    for cart_item in cart:
        cart_item.purchased = True
        cart_item.save()

    return render(request, 'Shop/success.html')

@csrf_exempt
def fail(request):
    return render(request, 'Shop/fail.html')