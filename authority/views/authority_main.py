from django.shortcuts import redirect
from datetime import timedelta
from datetime import date


# class-based view classes
from django.views.generic import TemplateView
from django.views.generic import ListView

# Permission and Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from django.contrib.auth.models import User
from ClothingApp.models import(
    Category,
    SubCategory,
    PRODUCT,
    OrderItem
)

from Clothing_Accounts.models import UserMessage


# Create your views here.
class AdminView(LoginRequiredMixin,AdminPassesTestMixin,TemplateView):
    template_name = 'authority/admin.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel" 
        context["user"] = self.request.user
        context["total_user"] = User.objects.all().count()
        context["total_product"] = PRODUCT.objects.all().count()
        context["total_order"] = OrderItem.objects.all().count()
        context["total_message"] = UserMessage.objects.all().count()
        context["last_orders"] = OrderItem.objects.filter(is_ordered=True).order_by('-id')[:10]
        return context
    




