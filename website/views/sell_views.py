from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.db import connection

from django.contrib.auth.models import User
from website.models import Product, Customer, ProductType
from website.forms import UserForm, ProductForm


def sell_product(request):
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        form_data = request.POST
        category = ProductType.objects.get(pk=1)

        p_form_data = {
            'title': form_data['title'],
            'description': form_data['description'],
            'price': form_data['price'],
            'quantity': form_data['quantity'],
        }
        product_form = ProductForm(p_form_data)

        if product_form.is_valid():
            print('++++++++++++++IM IN THE IF, SO IM VALID++++++++++++++++')
            customer_id = request.user.id
            productType_id = 1

            sql = "INSERT INTO website_product VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            product_params = [
                None,
                p_form_data['title'],
                p_form_data['description'],
                p_form_data['price'],
                p_form_data['quantity'],
                0,
                customer_id,
                productType_id
            ]

            with connection.cursor() as cursor:
                cursor.execute(sql, product_params)
        else:

            print("=============INVALID FORM DATA=========",
                  product_form.errors.as_json())
            template_name = 'product/create.html'
            return render(request, template_name, {'product_form': product_form})
        template_name = 'product/success.html'
        return render(request, template_name, {})
