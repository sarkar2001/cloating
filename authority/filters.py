import django_filters
from django import forms
from django.db.models import Q

from django.contrib.auth.models import User

from ClothingApp.models import(
    Category,
    SubCategory,
    ProductCategory,
    ProductSize,
    ProductColor,
    PRODUCT,
    OrderItem
    
)

class UserListFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_by_all_fields',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by email or first name'})
    )

    class Meta:
        model = User
        fields = ['search']

    def filter_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(email__icontains=value) | Q(first_name__icontains=value)
        )
        

class CategoryFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})
    )
    
    
    class Meta:
        model = Category
        fields = {
            'title': {'icontains'},
        }
        
        
class SubCategoryFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub-Category Name'})
    )
    
    
    class Meta:
        model = SubCategory
        fields = {
            'name': {'icontains'},
        }
        
class ProductCategoryFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub-Category Name'})
    )
    
    
    class Meta:
        model = ProductCategory
        fields = {
            'name': {'icontains'},
        }
        
class ProductSizeFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(
        field_name='size', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub-Category Name'})
    )
    
    
    class Meta:
        model = ProductSize
        fields = {
            'size': {'icontains'},
        }
        
class ProductColorFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(
        field_name='color', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub-Category Name'})
    )
    
    
    class Meta:
        model = ProductColor
        fields = {
            'color': {'icontains'},
        }
    

class ProductListFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'})
    )
    
    
    class Meta:
        model = PRODUCT
        fields = {
            'title',
            'condition'
        }
        
class OrderListFilter(django_filters.FilterSet):
    
    id = django_filters.CharFilter(
        field_name='id', 
        lookup_expr='exact', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order Id'})
    )
    
    
    class Meta:
        model = OrderItem
        fields = {
            'id',
            
        }
        
        


