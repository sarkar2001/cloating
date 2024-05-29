from django.contrib import admin
from .models import *

from .models import PRODUCT, ProductSize, ProductSizeThrough

# Register your models here.
# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(PRODUCT)
# admin.site.register(Cart)
# admin.site.register(Subsubcategory)
# admin.site.register(Variation)
admin.site.register(DeliveryAddress)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category','name']

# @admin.register(PRODUCT)
# class PRODUCTAdmin(admin.ModelAdmin):
#     list_display = ['id','title','product_category', 'condition','price','is_hot_deal']
@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'delivery_address', 'date', 'paymentSystem', 'delivery_fee', 'total', 'is_ordered']

    def display_order_items(self, obj):
        return ', '.join([str(item) for item in obj.order_item.all()])
    display_order_items.short_description = 'Order Items'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','subcategory']



class ProductSizeThroughInline(admin.TabularInline):
    model = ProductSizeThrough
    extra = 1

class PRODUCTAdmin(admin.ModelAdmin):
    inlines = [ProductSizeThroughInline]
    list_display = ['id','title', 'product_category', 'condition', 'price', 'is_hot_deal', 'is_trending']
    search_fields = ['title', 'description']
    list_filter = ['condition', 'is_hot_deal', 'is_trending']
    fieldsets = (
        (None, {
            'fields': ('title', 'product_category', 'image1', 'image2', 'image3', 'condition', 'price','discount','color', 'description', 'is_hot_deal', 'is_trending')
        }),
    )

admin.site.register(PRODUCT, PRODUCTAdmin)
admin.site.register(ProductSize)


