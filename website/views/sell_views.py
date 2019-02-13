from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.db import connection
from django.urls import reverse

from django.contrib.auth.models import User
from website.models import Product, Customer, ProductType
from website.forms import UserForm, ProductForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


def sell_product(request):
    """Handles displaying, validating, and posting the new product form

    Author(s): Nolan Little

    Arguments:
        request {request object}

    Returns:
        render -- if the request is a get, returns a render of the form
               -- if the request is a post, checks the validity of the form data
               -- if the data is valid, performs the db insert of new item and returns a render
                    of the details view of the new items
    """

    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        form_data = request.POST

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

        except MultiValueDictKeyError:
            myfile = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEbVj-dY-HFt1DhTc2JXe0LtqQ-HSDyMy1qvDNWJoFMtB7gfR9'
            uploaded_file_url = myfile

        p_form_data = {
            'title': form_data['title'],
            'description': form_data['description'],
            'price': form_data['price'],
            'quantity': form_data['quantity'],
            'category': form_data['category']
        }

        product_form = ProductForm(p_form_data)

        if product_form.is_valid():
            customer_id = request.user.id

            sql = "INSERT INTO website_product VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            product_params = [
                None,
                p_form_data['title'],
                p_form_data['description'],
                p_form_data['price'],
                p_form_data['quantity'],
                uploaded_file_url,
                0,    #default boolean not deleted
                customer_id,
                p_form_data['category']
            ]

            with connection.cursor() as cursor:
                cursor.execute(sql, product_params)
                product_id = cursor.lastrowid
        else:
            template_name = 'product/create.html'
            return render(request, template_name, {'product_form': product_form})

        product = Product.objects.raw('SELECT * FROM website_product WHERE id = %s', [product_id])
        template_name = 'product_details.html'
        return HttpResponseRedirect(reverse('website:product_details', args=(product_id,)))