from django import forms
from orders.models import Order
from django.utils.translation import gettext_lazy as _






class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name' , 'last_name' , 'phone_number' , 'address' , 'order_note']
        widgets = {
            'address': forms.Textarea(attrs={'rows':3 ,'class':'form-control'}),
            'order_note': forms.Textarea(attrs={
                'rows':4 ,
                'class':'form-control',
                'placeholder': _('If you have any notes please enter here otherwise leave empty'),
            })
        }



