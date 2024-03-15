from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(PRODUCT)
# admin.site.register(Cart)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category','name']

@admin.register(PRODUCT)
class PRODUCTAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','subcategory', 'condition','price']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']