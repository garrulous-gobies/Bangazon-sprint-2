from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm, PaymentForm
from website.models import Product
from django.db import connection

def profile(request, pk):
    """Lists profile information for current user. This uses raw SQL that does not correspond to a custom defined model. This does returns a list rather than a dictionary,
    so the dictionary must be created manually.
    Model: User model (built in, not a custom model)
    Template: profile.html
    Author(s): Zac Jones
    """
    
    with connection.cursor() as cursor:
            try:
                cursor.execute(f'''SELECT * FROM auth_user WHERE id = {pk}
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


def add_payment(request, pk):
    """[summary]
    
    Arguments:
        request {[type]} -- [description]
        pk {[type]} -- [description]

    Author(s): Austin Zoradi
    """
    if request.method == 'GET':
        payment_form = PaymentForm()
        context = {"payment_form": payment_form}
        return render(request, 'new_payment.html', context)
  
    
