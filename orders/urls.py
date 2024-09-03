from django.urls import path

from .views import *

urlpatterns = [
    path('create/' , order_create_view , name='order_create' ),
]