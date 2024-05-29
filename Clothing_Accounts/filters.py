import django_filters
from django import forms
from django.db.models import Q

from django.contrib.auth.models import User

from Clothing_Accounts.models import(
    SliderBanner,
    AboutUs,
    Brand,
    ContactUs,
    UserMessage
)

class SliderBannerFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Banner Title'})
    )
    
    
    class Meta:
        model = SliderBanner
        fields = {
            'title': {'icontains'},
        }
        
class AboutUsFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'About Title'})
    )
    
    
    class Meta:
        model = AboutUs
        fields = {
            'title': {'icontains'},
        }
        
        
class BrandFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'})
    )
    
    
    class Meta:
        model = Brand
        fields = {
            'name': {'icontains'},
        }
        
        
class ContactUsFilter(django_filters.FilterSet):
    
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'})
    )
    
    
    class Meta:
        model = ContactUs
        fields = {
            'title': {'icontains'},
        }
        
class UserMessageFilter(django_filters.FilterSet):
    
    email = django_filters.CharFilter(
        field_name='email', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Email'})
    )
    
    
    class Meta:
        model = UserMessage
        fields = {
            'email': {'icontains'},
        }