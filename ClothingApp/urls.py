from django.urls import path
from.views import *

urlpatterns = [
    path('product/<int:id>/', product, name='product'),
    path('single_product/<int:id>/', single_product, name='single_product'),
    path('addtocart/<int:id>/', addtocart, name='addtocart'),
    path('remove_cart/<int:id>/', remove_cart, name='remove_cart'),





]