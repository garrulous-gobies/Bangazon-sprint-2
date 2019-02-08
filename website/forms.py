from django.contrib.auth.models import User
from django import forms
from website.models import Product

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields =('title', 'description', 'price', 'quantity',)
        error_messages = {
            'price': {
                'min_value': "Price must be at least $0.02"
            },
            'quantity': {
                'min_value': "Quantity must be at least 1"
            },
        }