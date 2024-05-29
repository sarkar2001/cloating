from django import forms

from Clothing_Accounts.models import(
    SliderBanner,
    AboutUs,
    Brand,
    ContactUs
    
)


# forms
class SliderImageForm(forms.ModelForm):

    class Meta:
        model = SliderBanner
        fields = ('title','image', 'sale_offer', 'starting_price', )
        
class AboutForm(forms.ModelForm):

    class Meta:
        model = AboutUs
        fields = ('title', 'description', 'image', )
        
class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ('name', 'logo', )
        
        
class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('title', 'address', 'mobile', 'hotline', 'email', 'support_mail', )