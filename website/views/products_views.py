from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import *


def list_products(request):
    all_products = Product.objects.raw("SELECT * from website_product")
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})

def categories(request):
    """ Summary: This view selects all product categories and teh first three products. IT will display the categories, with the number of products in it, and the first three products.

    Modal(s): ProductType, Product

    Template: categories.html

    Author(s): Austin Zoradi
    """

    sql = """ SELECT *
              FROM "website_product"
    """

    sql2 = """SELECT *
              FROM "website_producttype"
    """

    sql3 = """SELECT *
               FROM "website_product"
               WHERE website_product.ProductType_id = %s
               LIMIT 3
    """

    all_products = Product.objects.raw(sql)
    all_productTypes = ProductType.objects.raw(sql2)

    limit_products_list = list()

    for cat_id in ProductType.objects.raw(sql2):
        limit_products = Product.objects.raw(sql3, [cat_id.id,])
        limit_products_list.append(limit_products)

    context = {"all_products": all_products, "all_productTypes": all_productTypes, "limit_products_list": limit_products_list}
    return render(request, 'categories.html', context)

def product_details(request, product_id):
    product = Product.objects.raw('''SELECT * from website_product p
                                            WHERE p.id = %s''', [product_id])[0]
    orders = ProductOrder.objects.raw('''SELECT * from website_productOrder p
                                        WHERE p.product_id = %s AND p.deleted=0''', [product_id])
    orderCount = len(orders)
    quantity = product.quantity - orderCount
    product.quantity = quantity
    # likedCount = ProductLike.objects.raw('''Select * from website_productlike
    #                                     WHERE website_productlike.product_id = %s''', [product_id])[0]
    # print("likedCount", likedCount)
    template_name = 'product_details.html'
    return render(request, template_name, {'product': product, 'product_id': product_id})


def category_list(request, productType_id):
    all_products = Product.objects.raw('''SELECT * from website_product
                                          WHERE website_product.producttype_id = %s''', [productType_id])
    category = ProductType.objects.raw('''Select * from website_producttype
                                          WHERE website_producttype.id = %s''', [productType_id])[0]
    for item in all_products:
        orders = ProductOrder.objects.raw('''SELECT * from website_productOrder p
                                        WHERE p.product_id = %s AND p.deleted=0''', [item.id])
        orderCount = len(orders)
        item.quantityRemaining = item.quantity - orderCount
    print("category",category.productCategory)
    template_name = 'category_list.html'
    return render(request, template_name, {'products': all_products, 'category': category})