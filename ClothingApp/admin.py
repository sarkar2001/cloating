from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(PRODUCT)
# admin.site.register(Cart)
# admin.site.register(Subsubcategory)
# admin.site.register(Variation)
admin.site.register(BillingInfo)
admin.site.register(Order)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category','name']

@admin.register(PRODUCT)
class PRODUCTAdmin(admin.ModelAdmin):
    list_display = ['id','title','product_category', 'condition','price','is_hot_deal']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'product', 'get_size', 'get_color', 'quantity']

    def get_size(self, obj):
        return obj.variation.size if obj.variation else "N/A"
    get_size.short_description = 'Size'

    def get_color(self, obj):
        return obj.variation.color if obj.variation else "N/A"
    get_color.short_description = 'Color'

@admin.register(ProductCategory)
class SubsubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','subcategory']

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['id','product','size','color','stock']