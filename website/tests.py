from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *
import unittest


class AddProductTest(TestCase):
    """Tests the "sell" form where a user adds a new product for sale

        Model(s): Product, ProductType, User

        Template(s): create.html, product_details.html

        Author(s): Nolan Little
    """


    def test_product_form_template(self):
        response = self.client.get(reverse('website:sell'))


    def test_product_form_validation(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        category = ProductType.objects.create(productCategory="Toys", deleted = 0)

        valid_response = self.client.post(reverse('website:sell'), {
            'title': 'bike',
            'description': 'It\'s a bike',
            'price': 10,
            'quantity': 1,
            'category': 1
            }
        )

        invalid_response = self.client.post(reverse('website:sell'), {
            'title': 'bike',
            'description': 'It\'s a bike',
            'price': 0,
            'quantity': -1,
            'category': 1
            }
        )

        self.assertEqual(valid_response.status_code, 302)

        self.assertEqual(invalid_response.status_code, 200)
        self.assertNotEqual(invalid_response.status_code, 302)

class OrderHistoryTest(TestCase):
    """Tests the order history view accessed from user profile

    Model(s): User, Order, ProductOrder, Product, PaymentType, PaymentMethod

    Template(s): order_history.html, order_history_detail.html

    Author(s): Nolan Little
    """

    def test_order_history_res(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        customer = Customer.objects.create(user=self.user, address="test", phoneNumber="test", deleted=0)
        category = ProductType.objects.create(productCategory="Toys", deleted = 0)
        pay_type = PaymentType.objects.create(paymentCategory="credit card", deleted = 0)
        payment_method = PaymentMethod.objects.create(accountNumber=1, customerPayment=customer, paymentName=pay_type)
        productType = ProductType.objects.create(productCategory="toys", deleted=0)
        product = Product.objects.create(
            title="bike",
            description="its a bike",
            price=1.00, quantity=1,
            image="https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544049078-gifts-for-brothers-jabra-ear-buds-1541438364.jpg?crop=1xw:1xh;center,top&resize=768:*",
            deleted=0,
            customer=self.user,
            productType= productType
        )
        order = Order.objects.create(deleted=0, customerOrder=customer, paymentOrder=payment_method)
        product_order = ProductOrder.objects.create(deleted=0, order=order, product=product)

        response = self.client.get(reverse('website:order_history', kwargs={'pk':self.user.id}))
        self.assertEqual(response.status_code, 200)

    def test_order_history_detail_res(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        customer = Customer.objects.create(user=self.user, address="test", phoneNumber="test", deleted=0)
        category = ProductType.objects.create(productCategory="Toys", deleted = 0)
        pay_type = PaymentType.objects.create(paymentCategory="credit card", deleted = 0)
        payment_method = PaymentMethod.objects.create(accountNumber=1, customerPayment=customer, paymentName=pay_type)
        productType = ProductType.objects.create(productCategory="toys", deleted=0)
        product = Product.objects.create(
            title="bike",
            description="its a bike",
            price=1.00, quantity=1,
            image="https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544049078-gifts-for-brothers-jabra-ear-buds-1541438364.jpg?crop=1xw:1xh;center,top&resize=768:*",
            deleted=0,
            customer=self.user,
            productType= productType
        )
        order = Order.objects.create(deleted=0, customerOrder=customer, paymentOrder=payment_method)
        product_order = ProductOrder.objects.create(deleted=0, order=order, product=product)

        response = self.client.get(reverse('website:order_history_details', kwargs={'pk':self.user.id, 'order_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_addition(self):
        a = 3
        b = 5
        c = a + b
        assert a + b == c