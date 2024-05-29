from django.urls import path
from.views import *

urlpatterns = [
    path('product/<int:id>/', product, name='product'),
    path('product/category/<int:id>/', category_details, name='category_details'),
    path('product/sub_category/<int:id>/', sub_category_details, name='sub_category_details'),
    path('product/product_category/<int:id>/', product_category_details, name='product_category_details'),
    path('single_product/<int:id>/', single_product, name='single_product'),
    # path('addtocart/<int:id>/', addtocart, name='addtocart'),
    path('addtocart/<int:product_id>/', addtocart, name='addtocart'),
    path('remove_cart/<int:id>/', remove_cart, name='remove_cart'),
    path('cart/', cart, name='cart'),
    path('minus_cart/<int:id>/', minus_cart, name='minus_cart'),
    path('plus_cart/<int:id>/', plus_cart, name='plus_cart'),
    path('brand/<int:id>/', brand, name='brand'),
    path('checkout/', checkout, name='checkout'),
    path('sslcommerz/', sslcommerz, name='sslcommerz'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
    path('Order/', fail, name='Order'),

]
