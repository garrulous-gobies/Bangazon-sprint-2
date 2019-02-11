from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product
from django.db import connection
from website.forms import ProfileForm, CustomerForm
from django.urls import reverse

def profile(request, pk):
    """Lists profile information for current user. This uses raw SQL that does not correspond to a custom defined model. This does returns a list rather than a dictionary,
    so the dictionary must be created manually.
    Model: User model (built in, not a custom model)
    Template: profile.html
    Author(s): Zac Jones
    """
    
    with connection.cursor() as cursor:
            try:
                cursor.execute(f'''SELECT * FROM auth_user JOIN website_customer ON auth_user.id = website_customer.user_id WHERE auth_user.id = {pk}
                            ''')
                
                columns = [col[0] for col in cursor.description]

                profile = dict()

                for row in cursor.fetchall():
                    to_add = dict(zip(columns, row))
                    profile.update(to_add)

            except connection.OperationalError as err:
                print("Error...", err)
    
    context = {"profile": profile}

    return render(request, 'profile.html', context)

def edit_profile(request, pk):

    with connection.cursor() as cursor:
            try:
                cursor.execute(f'''SELECT * FROM auth_user JOIN website_customer ON auth_user.id = website_customer.user_id WHERE auth_user.id = {pk}
                            ''')
                
                columns = [col[0] for col in cursor.description]

                profile = dict()

                for row in cursor.fetchall():
                    to_add = dict(zip(columns, row))
                    profile.update(to_add)

            except connection.OperationalError as err:
                print("Error...", err)

    profile_form = ProfileForm(
        initial={
            'first_name': profile['first_name'],
            'last_name': profile['last_name']
        }
    )
    customer_form = CustomerForm(
        initial={
            'address': profile['address'],
            'phoneNumber': profile['phoneNumber']
        }
    )

    context = {"profile_form": profile_form, "customer_form": customer_form}

    return render(request, 'profile_edit.html', context)

def submit_profile(request, pk):

    form_data = request.POST

    pro_form_data = {
        'first_name': form_data['first_name'],
        'last_name': form_data['last_name']
    }

    cust_form_data = {
        'address': form_data['address'],
        'phoneNumber': form_data['phoneNumber']
    }

    customer_id = request.user.id

    sql = "UPDATE auth_user SET first_name=%s, last_name=%s WHERE auth_user.id = %s"
    profile_params = [
        pro_form_data['first_name'],
        pro_form_data['last_name'],
        customer_id
    ]

    sql2 = "UPDATE website_customer SET address=%s, phoneNumber=%s WHERE user_id = %s"
    customer_params = [
        cust_form_data['address'],
        cust_form_data['phoneNumber'],
        customer_id
    ]

    print(profile_params)
    print(customer_params)

    with connection.cursor() as cursor:
        cursor.execute(sql, profile_params)
        cursor.execute(sql2, customer_params)


    return HttpResponseRedirect(reverse('website:profile', args=(pk,)))

  
    
