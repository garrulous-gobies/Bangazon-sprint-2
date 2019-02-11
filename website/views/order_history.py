from django.contrib.auth.models import User
from website.models import Order
from django.shortcuts import render


def order_history(request, pk):

    get_user_sql = '''
        SELECT * FROM auth_user
        WHERE id = %s
    '''
    user = User.objects.raw(get_user_sql, [pk])[0]

    get_orders_sql = '''
        SELECT * FROM website_order
        WHERE customerOrder_id = %s AND paymentOrder_id != %s
    '''
    orders = Order.objects.raw(get_orders_sql, [user.id, 1])

    context = {
        'user': user,
        'orders': orders
    }
    return render(request, 'order_history.html', context)

def order_history_details(request, pk, order_id):
    get_single_order_sql = '''
        SELECT * FROM website_order
        WHERE customerOrder_id = %s AND id = %s
    '''
    order = Order.objects.raw(get_single_order_sql, [pk, order_id])[0]
    context = {'order': order}
    return render(request, 'order_history_detail.html', context)
