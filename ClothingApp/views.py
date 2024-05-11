from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  # Import the login_required decorator


# Create your views here.


def product(request, id):
    user = request.user
    subcategory = SubCategory.objects.get(id=id)
    subsubcategory = Subsubcategory.objects.get(id=id)
    category = Category.objects.all()
    products = PRODUCT.objects.all()
    length = len(Cart.objects.filter(user=user))
    cart_details = Cart.objects.filter(user=user)[:2]
    all_cart = Cart.objects.filter(user=user)
    subtotal = sum(item.product.price * item.quantity for item in all_cart)
    if user.is_authenticated:
        context = {
            'products': products,
            'length': length,
            'cart_details': cart_details,
            'all_cart': all_cart,
            'subtotal': subtotal,
        }
    else:
        context = {
            'products': products,
        }

    prod = PRODUCT.objects.filter(subcategory=subcategory)
    return render(request, 'Shop/all_product.html', locals())


def single_product(request, id):
    user = request.user
    products = PRODUCT.objects.all()

    if user.is_authenticated:
        length = len(Cart.objects.filter(user=user))
        cart_details = Cart.objects.filter(user=user)[:2]
        all_cart = Cart.objects.filter(user=user)
        subtotal = sum(item.product.price * item.quantity for item in all_cart)

    single_product = PRODUCT.objects.get(id=id)

    if user.is_authenticated:
        context = {
            'products': products,
            'length': length,
            'cart_details': cart_details,
            'all_cart': all_cart,
            'subtotal': subtotal,
            'single_product': single_product
        }
    else:
        context = {
            'products': products,
            'single_product': single_product
        }

    return render(request, 'Shop/single_product.html', context)





@login_required
def addtocart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        size = request.POST.get('size', None)
        color = request.POST.get('color', None)

        product = PRODUCT.objects.get(pk=product_id)
        variation = None
        if size and color:
            variation = Variation.objects.filter(product=product, size=size, color=color).first()

        if variation:
            cart_item, created = Cart.objects.get_or_create(
                user=request.user,
                product=product,
                variation=variation
            )
            if not created:
                # If the cart item already exists, update the quantity
                cart_item.quantity += quantity
                cart_item.save()
                messages.success(request, "Quantity updated in cart.")
            else:
                cart_item.quantity = quantity
                cart_item.save()
                messages.success(request, "Item added to cart successfully.")
        else:
            messages.error(request, "Invalid variation.")

    else:
        messages.error(request, "Invalid request method.")

    return redirect('cart')



def add_to_cart(request, id):
    prod = PRODUCT.objects.get(id=id)
    user = request.user


    # if prod:
    #     if user.is_authenticated:
    #         try:
    #             cart = Cart.objects.get(Q(user=user) & Q(product=prod))
    #             if cart:
    #                 cart.quantity += 1
    #                 cart.save()
    #                 return redirect(request.META['HTTP_REFERER'])
    #         except:
    #             new_cart = Cart.objects.create(user=user, product=prod)
    #             new_cart.save()
    #             return redirect(request.META['HTTP_REFERER'])
    #     else:
    #         return redirect('Log_in')
    # return redirect(request.META['HTTP_REFERER'])

    if prod:
        if user.is_authenticated:
            if request.method == 'POST':
                # Get variation details from the form
                variation_id = request.POST.get('variation')
                size = request.POST.get('size')
                color = request.POST.get('color')
                quantity = int(request.POST.get('quantity', 1))

                # Fetch the variation object
                # variation = Variation.objects.get(id=variation_id)

                # Check if the item already exists in the cart
                cart_item = Cart.objects.filter(
                    Q(user=user) & Q(product=prod) & Q(size=size) & Q(color=color)).first()

                if cart_item:
                    # If item already exists, update the quantity
                    cart_item.quantity += quantity
                    cart_item.save()
                else:
                    # If item doesn't exist, create a new cart entry
                    Cart.objects.create(user=user, product=prod, size=size, color=color,
                                        quantity=quantity)

            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return redirect('Accounts/Log_in.html')  # Redirect to login page if user is not authenticated
    else:
        return redirect('home.html')  # Redirect to home page if product does not exist



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

                elif length > 1:
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
                'fail_url': "http://127.0.0.1:8020/ClothingApp/fail/",
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


def Customer(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        company_name= request.POST.get('company_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postcode = request.POST.get('postcode')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        customer = Customer(
            firstname=firstname,
            lastname=lastname,
            company_name=company_name,
            address=address,
            city=city,
            country=country,
            postcode=postcode,
            email=email,
            phone=phone
        )
        customer.save()

        # Redirect to a success page or do something else
        return redirect('order_success')

    return render(request, 'Shop/checkout.html')

#
# # Example of reducing stock when an order is placed
# def place_order(request):
#     # Logic to place order
#     # Assuming you have a product_id, color, and size in your request
#     product = Product.objects.get(pk=request.POST['product_id'])
#     variation = product.stockvariation_set.get(color=request.POST['color'], size=request.POST['size'])
#     variation.stock_quantity -= 1
#     variation.save()

