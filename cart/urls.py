
from django.urls import  path

from .views import *


app_name = 'cart'

urlpatterns = [
    path('' , cart_detail_view , name='cart_detail'),
    path('add/<int:product_id>/' , add_to_cart_view ,name='cart_add'),

    path('remove/' , remove_all_cart_view ,name='cart_all_remove'),
    path('remove/<int:product_id>/' , remove_from_cart_view ,name='cart_remove'),
]