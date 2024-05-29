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

#Import Filter Classes
from authority.filters import UserListFilter


# Models Accounts
from django.contrib.auth.models import User

#Import From
from authority.forms import UserInfoForm


class UserListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = User.objects.filter(is_active=True)
    filterset_class = UserListFilter
    template_name = 'user/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User List"
        context["user_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context


class EditUserInfoView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    form_class = UserInfoForm
    template_name = 'user/update_user.html'
    success_url = reverse_lazy('authority:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add User Info"
        user_object = User.objects.get(id=self.kwargs.get('pk'))
        context["form"] = self.form_class(instance=user_object)
        return context
         
    # def post(self, request, *args, **kwargs):
    #     user_object = User.objects.get(id=self.kwargs.get('pk'))
    #     form = self.form_class(request.POST, request.FILES, instance=user_object.profile)
    #     form2 = self.form_class2(request.POST, request.FILES, instance=user_object.employee_info)
    #     return self.form_valid(form, form2)
    
    def form_valid(self, form):
        messages.success(self.request, "User Info Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try again")
        return super().form_invalid(form)