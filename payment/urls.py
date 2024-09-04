from django.urls import path

from cart.urls import app_name
from .views import  *

app_name = 'payment'

urlpatterns = [
    path('process/' , payment_process , name='payment_process'),
    path('callback/' , payment_callback_view , name='payment_callback'),
]