from django import forms


# models
from django.contrib.auth.models import User
from ClothingApp.models import(
    Category,
    SubCategory,
    ProductCategory,
    ProductSize,
    ProductColor,
    PRODUCT
    
)

# forms
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','is_staff')
        

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('title',)
        
class SubCategoryForm(forms.ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ('name','category')
        
class ProductCategoryForm(forms.ModelForm):
    
    class Meta:
        model = ProductCategory
        fields = ('name','subcategory')
        
        
class ProductSizeForm(forms.ModelForm):
    
    class Meta:
        model = ProductSize
        fields = ('size',)
        
class ProductColorForm(forms.ModelForm):
    
    class Meta:
        model = ProductColor
        fields = ('color',)


# Product Forms
class ProductFrom(forms.ModelForm):
    
    class Meta:
        model = PRODUCT
        fields = ('title','product_category','image1','image2','image3','condition','price','description','is_hot_deal','is_trending')
