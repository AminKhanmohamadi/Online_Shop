from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import OrderItem
from cart.cart import Cart
from .forms import OrderForm

# Create your views here.
@login_required
def order_create_view(request):


    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('There are no orders in your cart.'))
        return redirect('product-list')

    initial_data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    }
    order_form = OrderForm(request.POST or None, initial=initial_data)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj =order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart :
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price = product.price
                )
            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')

    return render(request, 'orders/order_create.html' , {'form': order_form} )
