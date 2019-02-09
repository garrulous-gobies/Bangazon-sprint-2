from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

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
    """This view will display a form to add a new payment option when the button is clicked. The form includes an input field for the account number and a dropdown of all the types of payments in the db. When the request is a POST (when the save button is clicked) the form saves the input the db for the user.
    
    Arguments: pk {[primary key]} -- the user's Id
    
    Modal(s): PaymentMathods, PaymentType

    Form(s): PaymentForm

    Template(s): new_payment.html

    Author(s): Austin Zoradi
    """
    if request.method == 'GET':
        payment_form = PaymentForm()
        context = {"payment_form": payment_form}
        return render(request, 'new_payment.html', context)

    elif request.method == 'POST':
        form_data = request.POST
        pt_form_data = {
          "accountNumber": form_data["accountNumber"],
          "paymentName": form_data["paymentName"] 
        }


        # customer_id = request.user.id
        sql = "INSERT INTO website_paymentmethod VALUES (%s,%s,%s,%s,%s)"
        payment_params = [
            None,
            pt_form_data['accountNumber'],
            0,
            pk,
            pt_form_data["paymentName"]
        ]
        
        with connection.cursor() as cursor:
            cursor.execute(sql, payment_params)

        return render(request, 'profile.html', {})

  
    
