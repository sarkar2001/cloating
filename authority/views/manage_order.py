from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

# class-based view classes
from django.views.generic import DetailView
from django.views.generic import ListView



# Permission and Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from ClothingApp.models import OrderItem, Cart


from authority.filters import OrderListFilter

   


#<<----------------- List, Add, Update Category ---------------->>
class OrderListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = OrderItem.objects.filter(is_ordered=True).order_by('-id')
    filterset_class =OrderListFilter
    template_name = 'orders/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Order List"
        context["orders_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    

class OrderDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    queryset = OrderItem.objects.all()
    template_name = 'orders/order_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Order Details"
        context["order"] = OrderItem.objects.get(id=self.kwargs.get('pk'))
        
        return context