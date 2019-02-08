from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product
from django.db import connection
from website.forms import ProfileForm
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

    profile_form = ProfileForm()

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
    

    context = {"profile": profile, "profile_form": profile_form}

    return render(request, 'profile_edit.html', context)

def submit_profile(request, pk):

    form_data = request.POST

    pro_form_data = {
        'first_name': form_data['first_name'],
        'last_name': form_data['last_name']
    }

    print(pro_form_data)

    customer_id = request.user.id

    sql = "UPDATE auth_user SET (%s, %s, %s) WHERE auth_user.id = {customer_id}"
    profile_params = [
        None,
        pro_form_data['first_name'],
        pro_form_data['last_name']
    ]

    with connection.cursor() as cursor:
        cursor.execute(sql, profile_params)
        # product_id = cursor.lastrowid



    context = {"boi": "hey"}
    return HttpResponseRedirect(reverse('website:profile', args=(pk,)))

  
    
