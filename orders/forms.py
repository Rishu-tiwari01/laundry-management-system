from django import forms
from django.core.validators import RegexValidator
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'garment', 'quantity', 'price_per_item', 'status']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 9876543210'
            }),
            'garment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Shirt, Pants, Saree'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': '1'
            }),
            'price_per_item': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0.01',
                'step': '0.01',
                'placeholder': '50.00'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Name must be at least 2 characters')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        import re
        if not re.match(r'^\+?[0-9]{10,15}$', phone):
            raise forms.ValidationError('Enter a valid phone number (10-15 digits)')
        return phone

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity < 1:
            raise forms.ValidationError('Quantity must be at least 1')
        return quantity

    def clean_price_per_item(self):
        price = self.cleaned_data.get('price_per_item')
        if price is None or price <= 0:
            raise forms.ValidationError('Price must be greater than 0')
        return price

    def clean_garment(self):
        garment = self.cleaned_data.get('garment', '').strip()
        if len(garment) < 2:
            raise forms.ValidationError('Garment type must be at least 2 characters')
        return garment
