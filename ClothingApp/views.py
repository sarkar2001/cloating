from django.shortcuts import render,redirect
from .models import *
from django.db.model import Q
# Create your views here.

def product(request, id):
    prod = PRODUCT.objects.filter(category=id)
    return render(request, 'Shop/all_product.html', locals())


def single_product(request, id):
    single_product = PRODUCT.objects.get(id=id)
    return render(request, 'Shop/single_product.html', locals())

def AddtoCart(request, id):
   pass






