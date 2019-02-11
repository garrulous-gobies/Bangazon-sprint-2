from django.contrib.auth.models import User
from website.models import Product, Customer, ProductType
from django.shortcuts import render


def order_history(request, pk):

    sql = '''
        SELECT * FROM auth_user
        WHERE id = %s
    '''

    user = User.objects.raw(sql, [pk])
    context = {'user': user}
    return render(request, 'order_history.html', context)
