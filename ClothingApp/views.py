from django.shortcuts import render
from .models import *
# Create your views here.

def product(request, id):
    prod = PRODUCT.objects.filter(category=id)
    return render(request, 'Shop/all_product.html', locals())




