from django.urls import path

from .views import *

urlpatterns = [
    path('' , ProductListView.as_view(), name='product-list'),
    path('<int:pk>' , ProductDetailView.as_view(), name='product-detail'),
    path('comment/<int:product_id>/' , CommentCreateView.as_view(), name='comment-create'),

    path('hello/' , hello, name='hello'),

]