from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import UserForm, ProductForm
from website.models import Product


def cart(request, pk):
    context = {"cart": "hotdog"}
    return render(request, 'cart.html', context )