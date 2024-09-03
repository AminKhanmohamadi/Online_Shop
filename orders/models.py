from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from products.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , verbose_name=_('User'))

    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))

    phone_number = PhoneNumberField(verbose_name=_('Phone Number'))

    address = models.CharField(max_length=700, verbose_name=_('Address'))

    is_paid = models.BooleanField(default=False , verbose_name=_('Is Paid'))

    order_note = models.TextField(verbose_name=_('Description') , blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'Order {self.id} - {self.user} : {self.is_paid}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Order'), related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='order_items')
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity') , default=1)
    price = models.PositiveIntegerField(verbose_name=_('Price'))

    def __str__(self):
        return f'OrderItem {self.id}: for product {self.product} * {self.quantity} (price: {self.price})'

    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')

