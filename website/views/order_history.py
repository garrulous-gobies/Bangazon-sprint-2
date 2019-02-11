from django.contrib.auth.models import User
from website.models import Order
from django.shortcuts import render
from decimal import Decimal


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

    order_total = get_order_total(order)
    context = {'order': order, 'order_total': order_total}
    return render(request, 'order_history_detail.html', context)



# ===========================helper functions========================
def get_order_total(order):
    """Calculates total of all the product prices and tax in the gven order

    Author(s): Nolan Little

    Arguments:
        order {Object} -- Single Order instance from the database

    Returns:
        dictionary -- sub_total = combined price of all objects, tax = calculated tax, total = final total(sub + tax)
    """

    tax_rate = Decimal(.0945)
    sub_total = 0
    order_total = dict()

    for product_order in order.productorder_set.all():
        sub_total += product_order.product.price

    order_total['sub_total'] = sub_total
    order_total['tax'] = round(sub_total * tax_rate, 2)
    order_total['total'] = round(sub_total + (sub_total * tax_rate), 2)

    return order_total