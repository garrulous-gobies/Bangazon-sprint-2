from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Order, ProductOrder, Product
import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


def cart(request, user_id):
    order = Order.objects.raw('''SELECT * from website_order o
                                WHERE o.customerOrder_id = %s AND o.paymentOrder_id = 1''', [user_id])
    order = order[0].id
    all_product_orders = ProductOrder.objects.raw('''SELECT * from website_productorder po
                                                    WHERE po.order_id = %s''', [order])
    all_products = []
    for product in all_product_orders:
        item = Product.objects.raw('''SELECT * from website_product p
                                            WHERE p.id = %s''', [product.id])
        item = item[0]
        all_products.append(item)
    context = {"products_in_cart": all_products}
    # context = {"products_in_cart": order}
    return render(request, 'cart.html', context )