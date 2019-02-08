from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product

def index(request):
    template_name = 'index.html'
    all_products = Product.objects.raw('''SELECT *
                                        from website_product
                                        ORDER BY id
                                        DESC LIMIT 20''')
    return render(request, template_name, {'products': all_products})














