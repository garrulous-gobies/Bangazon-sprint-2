from django.contrib.auth.models import User
from django import forms
from website.models import Product, Customer, ProductType

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('address', 'phoneNumber',)



class ProductForm(forms.ModelForm):
    """Form class for a user adding a new prodcut to sell

    Author(s): Nolan Little

    """

    # generate a tuple of tuples to populate the dropdown field with product categories.
    def get_categories():
        sql = 'SELECT id, productCategory FROM website_producttype'
        product_types = ProductType.objects.raw(sql, None)
        choices = [('', 'select category')]
        for p in product_types:
            product_choice = (p.id, p.productCategory)
            choices.append(product_choice)
        choices = tuple(choices)
        return choices

    category = forms.ChoiceField(choices=get_categories)

    class Meta:
        model = Product
        fields =('title', 'description', 'price', 'quantity','category')
        error_messages = {
            'price': {
                'min_value': "Price must be at least $0.02"
            },
            'quantity': {
                'min_value': "Quantity must be at least 1"
            },
        }