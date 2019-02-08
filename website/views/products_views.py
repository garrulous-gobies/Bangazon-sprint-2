from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product, ProductType


def list_products(request):
    all_products = Product.objects.all()
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
    product = get_object_or_404(Product, id=product_id)
    template_name = 'product_details.html'
    return render(request, template_name, {'product': product})
