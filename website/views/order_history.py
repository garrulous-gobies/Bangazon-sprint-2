from django.contrib.auth.models import User
from website.models import Order
from django.shortcuts import render
from decimal import Decimal


def order_history(request, pk):
    """A list of the users orders

    Author(s): Nolan Little

    Arguments:
        request {object} -- request object
        pk {int} -- user id

    template: 'order_history.html'

    Returns:
        render -- 'order_history.html'
    """
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

    order_totals = dict()
    for order in orders:
        order_totals[order.id] = get_order_total(order)

    context = {
        'user': user,
        'orders': orders,
        'order_totals': order_totals
    }
    return render(request, 'order_history.html', context)


def order_history_details(request, pk, order_id):
    """Details of past order in users order history

    Author(s): Nolan Little

    Arguments:
        request {object} -- request object
        pk {int} -- user id
        order_id {int} -- id of order

    template: 'order_history_detail.html'

    Returns:
        render -- 'order_history_detail.html'
    """

    get_single_order_sql = '''
        SELECT * FROM website_order
        WHERE customerOrder_id = %s AND id = %s
    '''
    order = Order.objects.raw(get_single_order_sql, [pk, order_id])[0]

    truncated_acct_num = str(order.paymentOrder.accountNumber)[-4:]
    num_hidden_acct_chars= (len(str(order.paymentOrder.accountNumber)) - 4)

    star_chars = ''
    i = 0
    while i < num_hidden_acct_chars:
        star_chars += '*'
        i +=1

    order_total = get_order_total(order)

    context = {
        'order': order,
        'order_total': order_total,
        'truncated_acct_num': truncated_acct_num,
        'star_chars': star_chars
    }
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
