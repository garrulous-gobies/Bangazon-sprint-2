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
        self.assertIn(
            '<p><label for="id_title">Title:</label> <input type="text" name="title" maxlength="80" required id="id_title"></p>\n<p><label for="id_description">Description:</label> <textarea name="description" cols="40" rows="10" id="id_description">\n</textarea></p>\n<p><label for="id_price">Price:</label> <input type="number" name="price" step="0.01" required id="id_price"></p>\n<p><label for="id_quantity">Quantity:</label> <input type="number" name="quantity" min="0" required id="id_quantity"></p>\n<p><label for="id_category">Category:</label> <select name="category" required id="id_category">\n  <option value="" selected>select category</option>\n\n</select></p>\n    <input type="submit" value="Sell It" />'.encode(), response.content
            )

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

