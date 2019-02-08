from django.contrib.auth.models import User
from django import forms
from website.models import Product, Customer, PaymentMethod, PaymentType

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

class PaymentForm(forms.ModelForm):
    def getPaymentType():
        sql = "SELECT * FROM website_paymenttype"
        payment_types = PaymentType.objects.raw(sql)
        print(payment_types)
        choices = [("", "Select a Payment Type")]

        for choice in payment_types:
            item = (choice.id, choice.paymentCategory)
            choices.append(item)

        return choices
    
    paymentName = forms.ChoiceField(choices=getPaymentType)
    
    class Meta:
        model = PaymentMethod
        fields = ('accountNumber', 'paymentName')