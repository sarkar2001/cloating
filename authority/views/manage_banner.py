from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

# class-based view classes
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Permission and Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from Clothing_Accounts.models import (
    SliderBanner,
    AboutUs,
    Brand,
    ContactUs
)



# Import Filters
from Clothing_Accounts.filters import(
    SliderBannerFilter,
    AboutUsFilter,
    BrandFilter,
    ContactUsFilter
)

   


#Import Forms
from Clothing_Accounts.forms import (
    SliderImageForm,
    AboutForm,
    BrandForm, 
    ContactUsForm
)


#<<----------------- List, Add, Update Category ---------------->>
class SliderBannerListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = SliderBanner.objects.all()
    filterset_class =SliderBannerFilter
    template_name = 'fontend/banner_image_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Banner Image List"
        context["banner_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class UpdateBannerImageView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= SliderBanner
    form_class= SliderImageForm
    template_name='fontend/add_update_banner_image.html'
    success_url= reverse_lazy('authority:banner_image_list')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Banner Image"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Slider Image Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddBannerImageView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = SliderBanner
    form_class = SliderImageForm
    template_name = 'fontend/add_update_banner_image.html'
    success_url = reverse_lazy('authority:banner_image_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Slider Banner"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Slider Banner Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
    
    
#<<----------------- List, Add, Update About Us ---------------->>
class AboutListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = AboutUs.objects.all()
    filterset_class =AboutUsFilter
    template_name = 'fontend/about_us_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About List"
        context["about_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context


class UpdateAboutUsView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= AboutUs
    form_class= AboutForm
    template_name='fontend/add_update_about_us.html'
    success_url= reverse_lazy('authority:about_us_list')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update About Us"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "About Us Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddAboutUsView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = AboutUs
    form_class = AboutForm
    template_name = 'fontend/add_update_about_us.html'
    success_url = reverse_lazy('authority:about_us_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add About Us"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "About Us Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
    
#<<----------------- List, Add, Update Brand ---------------->>
class BrandListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = Brand.objects.all()
    filterset_class =BrandFilter
    template_name = 'fontend/brand_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Brand List"
        context["brand_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context


class UpdateBrandView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= Brand
    form_class= BrandForm
    template_name='fontend/add_update_brand.html'
    success_url= reverse_lazy('authority:brand_list')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Brand"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Brand Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddBrandView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model =Brand
    form_class = BrandForm
    template_name = 'fontend/add_update_brand.html'
    success_url = reverse_lazy('authority:brand_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Brand"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Brand Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
    
    
#<<----------------- List, Add, Update Contact Us ---------------->>
class ContactUsListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = ContactUs.objects.all()
    filterset_class =ContactUsFilter
    template_name = 'fontend/contact_us_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us List"
        context["contact_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context


class UpdateContactUsView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= ContactUs
    form_class= ContactUsForm
    template_name='fontend/add_update_contact_us.html'
    success_url= reverse_lazy('authority:contact_us_list')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Contact Us"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Contact Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddContactUsView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model =ContactUs
    form_class = ContactUsForm
    template_name = 'fontend/add_update_contact_us.html'
    success_url = reverse_lazy('authority:contact_us_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Contact Us"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Contact Info Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)