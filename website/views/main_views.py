from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.forms import UserForm, ProductForm
from website.models import *

def index(request):
    template_name = 'index.html'
    all_products = Product.objects.raw('''SELECT *
                                        from website_product
                                        ORDER BY id
                                        DESC LIMIT 20''')
    for product in all_products:
        product.likedAverage = ""
        allRatings = ProductLike.objects.raw('''SELECT * from website_productlike p
                                            WHERE p.product_id = %s''', [product.id])
        if len(allRatings) > 0:
            ratingCount = 0
            totalRating = 0
            for item in allRatings:
                totalRating += item.liked
                ratingCount += 1
            ratingAverage = totalRating / ratingCount
            starPrint = 0
            while ratingAverage > 0:
                if ratingAverage > .75:
                    product.likedAverage += '<img class="list_rating_star" src="../static/website/goldStar.png" alt="Gold Star">'
                    ratingAverage -= 1
                    starPrint += 1
                elif ratingAverage > .25:
                    product.likedAverage += '<img class="list_rating_star" src="../static/website/halfStar.png" alt="Half Star">'
                    ratingAverage = 0
                    starPrint += 1
            while starPrint != 5:
                product.likedAverage += '<img class="list_rating_star" src="../static/website/whiteStar.png" alt="White Star">'
                starPrint += 1
        else:
            starPrint = 0
            while starPrint != 5:
                product.likedAverage += '<img class="list_rating_star" src="../static/website/whiteStar.png" alt="White Star">'
                starPrint += 1
    return render(request, template_name, {'products': all_products})














