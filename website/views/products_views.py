from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product, ProductType


def list_products(request):
    all_products = Product.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})

def categories(request):
    sql = """ SELECT * 
              FROM "website_product"
    """

    products_in_cat = """SELECT count(website_product.id)
                         FROM "website_product"
                         WHERE website_product.productType_id = website_producttype.id
    """
    sql2 = """SELECT * FROM "website_producttype"
    """
    product_in_category = Product.objects.raw(products_in_cat)
    all_products = Product.objects.raw(sql)
    all_productTypes = ProductType.objects.raw(sql2)
    context = {"all_products": all_products, "all_productTypes": all_productTypes, "product_in_category":product_in_category}
    return render(request, 'categories.html', context)