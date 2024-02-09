from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('Log_in/', Log_in, name='Log_in'),
    path('log_out/', log_out, name='log_out'),
    path('Registration/', Registration, name='Registration'),

]