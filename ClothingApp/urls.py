from django.urls import path
from.views import *

urlpatterns = [
    path('product/<int:id>/', product, name='product'),
    path('single_product/<int:id>/', single_product, name='single_product'),



]