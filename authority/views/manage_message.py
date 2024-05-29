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
    UserMessage

)



# Import Filters
from Clothing_Accounts.filters import(
    UserMessageFilter
)

   


#<<----------------- List, Add, Update Category ---------------->>
class MassageListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = UserMessage.objects.all()
    filterset_class =UserMessageFilter
    template_name = 'customer_message/message_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer Message"
        context["message_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    

class MessageDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    queryset = UserMessage.objects.all()
    template_name = 'customer_message/message_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Message Details"
        context["message"] = UserMessage.objects.get(id=self.kwargs.get('pk'))
        
        return context


