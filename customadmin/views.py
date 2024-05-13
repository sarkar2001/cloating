from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from ClothingApp.models import *
from Clothing_Accounts.models import *

# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                messages.success(request, "You are Successfully logged in!")
                return redirect('login.html')
            else:
                return redirect('login.html')
        else:
            messages.warning(request, "No User Found!")
            return redirect('customadmin/login.html')
    return render(request, 'customadmin/login.html')
