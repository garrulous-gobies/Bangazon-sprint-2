from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product


def list_products(request):
    all_products = Product.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})

def categories(request):
    context = {"categories":"all the things"}
    return render(request, 'categories.html', context)

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    template_name = 'product_details.html'
    return render(request, template_name, {'product': product})
