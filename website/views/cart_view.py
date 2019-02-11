from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from website.forms import UserForm, ProductForm
from website.models import Order, ProductOrder, Product, PaymentMethod
import sqlite3
from decimal import *


conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c = conn.cursor()


def cart(request):
    user_id = request.user.id
    order = Order.objects.raw('''SELECT * from website_order o
                                WHERE o.customerOrder_id = %s AND o.paymentOrder_id = 1 AND o.deleted = 0''', [user_id])
    count = len(order)
    if count > 0:
        order = order[0].id
        all_product_orders = ProductOrder.objects.raw('''SELECT * from website_productorder po
                                                        WHERE po.order_id = %s AND po.deleted = 0''', [order])
        all_products = []
        total = 0
        count = 0
        for product in all_product_orders:
            item = Product.objects.raw('''SELECT * from website_product p
                                                WHERE p.id = %s''', [product.product_id])
            item = item[0]
            total += item.price
            count += 1
            item.order_id = product.id
            all_products.append(item)
        tax = Decimal(.0945)
        tax = round(total * tax, 2)
        total_with_tax = total + tax
        if count == 0:
            empty = "Your Bangazon Cart Is Empty"
        else:
            empty = "Your Bangazon Cart"
        context = {"products_in_cart": all_products, "total": total, "count": count, "tax": tax, "total_with_tax": total_with_tax, "empty": empty}
        return render(request, 'cart.html', context )
    else:
        cart = Order(deleted=0, customerOrder_id=user_id, paymentOrder_id=1)
        cart.save()
        return HttpResponseRedirect(reverse('website:cart'))

def add_to_cart(request, product_id):
    user_id = request.user.id
    order = Order.objects.raw('''SELECT * from website_order o
                                WHERE o.customerOrder_id = %s AND o.paymentOrder_id = 1 AND o.deleted = 0''', [user_id])
    count = len(order)
    print("count", count)
    if count == 0:
        cart = Order(deleted=0, customerOrder_id=user_id, paymentOrder_id=1)
        cart.save()
        order = Order.objects.raw('''SELECT * from website_order o
                                WHERE o.customerOrder_id = %s AND o.paymentOrder_id = 1 AND o.deleted = 0''', [user_id])
    order = order[0].id
    product = ProductOrder(deleted=0, order_id=order, product_id=product_id)
    product.save()
    return HttpResponseRedirect(reverse('website:cart'))

def remove_from_cart(request, order_id):
    ProductOrder.objects.filter(id=order_id).update(deleted=1)
    return HttpResponseRedirect(reverse('website:cart'))

def select_payment(request, pk):
    sql = """ SELECT *, LENGTH(pm.accountNumber) as account_num_length
              FROM website_paymentmethod pm
              JOIN website_paymenttype pt
              ON pm.paymentName_id = pt.id
              WHERE customerPayment_id = %s
    """

    # sql2="""SELECT LENGTH(pm.accountNumber)
    #         from website_paymentmethod pm
    #         WHERE customerPayment_id = %s
    # """

    payment_types= PaymentMethod.objects.raw(sql, [pk,])
    # account_num_length = PaymentMethod.objects.raw(sql2, [pk,])
    for option in payment_types:
        anum = str(option.accountNumber)
        strlength = len(anum)
        masked = strlength - 4
        slimstr = anum[masked:]
        print("*", * masked + slimstr)
        # maskedNum = * masked + slimstr
        # return maskedNum

    context = {"payment_types": payment_types}
    return render(request, 'complete_order.html', context)
