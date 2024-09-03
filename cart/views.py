from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST

from products.models import Product
from django.utils.translation import gettext_lazy as _
from .cart import Cart
from .forms import AddToCartProductForm
# Create your views here.


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace' : True,
        })

    context = {'cart': cart}
    return render(request , 'cart/cart.html' , context)

@require_POST
def add_to_cart_view(request , product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity , replace_current_quantity=cleaned_data['inplace'])
        messages.success(request, _('Successfully added to cart'))

    return redirect('cart:cart_detail')

def remove_from_cart_view(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    cart.remove(product)
    messages.error(request , _('Successfully removed from cart') )

    return redirect('cart:cart_detail')



def remove_all_cart_view(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _('Successfully all removed from cart'))
    else:
        messages.warning(request ,_('Your cart is already empty'))
    return redirect('cart:cart_detail')