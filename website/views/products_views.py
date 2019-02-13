from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext
from django.urls import reverse
from website.forms import *
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

    sql1 = """SELECT *
              FROM "website_producttype"
    """

    sql2 = """SELECT *
               FROM "website_product"
               WHERE website_product.ProductType_id = %s
               LIMIT 3
    """

    all_productTypes = ProductType.objects.raw(sql1)

    limit_products_list = list()

    for cat_id in ProductType.objects.raw(sql1):
        limit_products = Product.objects.raw(sql2, [cat_id.id,])
        limit_products_list.append(limit_products)

    context = {"all_productTypes": all_productTypes, "limit_products_list": limit_products_list}
    return render(request, 'categories.html', context)

def product_details(request, product_id):
    user_id = request.user.id
    liked = ""
    try:
        likeCount = ProductLike.objects.raw('''SELECT * from website_productlike p
                                            WHERE p.product_id = %s AND p.user_id = %s''', [product_id, user_id])[0]
        ratings = likeCount
        rate = likeCount.liked
        starPrint = 0
        while rate > 0:
            if rate > .75:
                liked += '<img class="rating_star" src="../static/website/goldStar.png" alt="Gold Star">'
                rate -= 1
                starPrint += 1
            elif rate > .25:
                liked += '<img class="rating_star" src="../static/website/halfStar.png" alt="Half Star">'
                rate = 0
                starPrint += 1
        while starPrint != 5:
            liked += '<img class="rating_star" src="../static/website/whiteStar.png" alt="White Star">'
            starPrint += 1
    except:
        ratings = "Null"
        starPrint = 0
        while starPrint != 5:
            liked += '<img class="rating_star" src="../static/website/whiteStar.png" alt="White Star">'
            starPrint += 1
    product = Product.objects.raw('''SELECT * from website_product p
                                            WHERE p.id = %s''', [product_id])[0]
    orders = ProductOrder.objects.raw('''SELECT * from website_productOrder p
                                    left join website_order o
                                    on o.id = p.order_id
                                    WHERE p.product_id = %s AND p.deleted=0 AND o.paymentOrder_id != 1''', [product.id])
    orderCount = len(orders)
    quantity = product.quantity - orderCount
    product.quantity = quantity
    template_name = 'product_details.html'
    return render(request, template_name, {'product': product, 'product_id': product_id, 'liked': liked, 'ratings': ratings})


def category_list(request, productType_id):
    all_products = Product.objects.raw('''SELECT * from website_product
                                          WHERE website_product.producttype_id = %s''', [productType_id])
    category = ProductType.objects.raw('''Select * from website_producttype
                                          WHERE website_producttype.id = %s''', [productType_id])[0]
    for item in all_products:
        orders = ProductOrder.objects.raw('''SELECT * from website_productOrder p
	                                        left join website_order o
	                                        on o.id = p.order_id
                                            WHERE p.product_id = %s AND p.deleted=0 AND o.paymentOrder_id != 1''', [item.id])
        orderCount = len(orders)
        item.quantityRemaining = item.quantity - orderCount
    template_name = 'category_list.html'
    return render(request, template_name, {'products': all_products, 'category': category})

def search_products(request):
    """Summary: Allows user to search through all products.
    
    Arguments:
        request -- request object

    Author(s): Austin Zoradi
    """
    if request.POST:
        sql = """ SELECT *
                  FROM website_product
                  WHERE website_product.title like %s 
                  OR website_product.description like %s
        """

        search_param = request.POST["Search"]
        search_param = '%' + search_param + '%'
       

        product_list = Product.objects.raw(sql, [search_param, search_param])
        print(product_list, "+++++++++++++++++++++++++++++++++++++++++++++")
        context={"product_list": product_list}

    return render(request, "searched_product.html", context)
            
            
def edit_ratings(request, product_id):
    user_id = request.user.id

    try:
        item = ProductLike.objects.raw('''SELECT * from website_productlike p
                                            WHERE p.product_id = %s AND p.user_id = %s''', [product_id, user_id])[0]
        comment = item.comment
        liked = item.liked
    except:
        liked = 0
        comment = ""
    return render(request, 'edit_rating.html', {'user_id': user_id, 'product_id': product_id, 'liked': liked, 'comment': comment})

def save_edits(request):
    user_id = request.POST['user_id']
    product_id = request.POST['product_id']
    liked = request.POST['liked']
    comment = request.POST['comment']
    try:
        item = ProductLike.objects.raw('''SELECT * from website_productlike p
                                            WHERE p.product_id = %s AND p.user_id = %s''', [product_id, user_id])[0]
        item.comment = comment
        item.liked = liked
        item.save()
    except:
        newInfo = ProductLike(liked=liked, comment=comment, product_id=product_id, user_id=user_id)
        newInfo.save()
    print("userId", user_id)
    print("productId", product_id)
    print("liked", liked)
    print("comment", comment)
    product_id = int(product_id)
    return redirect('website:product_details', product_id=product_id)
    # return HttpResponseRedirect(reverse('website:product_details', *args(product_id)))
