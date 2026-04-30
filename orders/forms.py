from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name','phone','garment','quantity','price_per_item','status']