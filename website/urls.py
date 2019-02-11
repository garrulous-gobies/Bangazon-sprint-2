from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^products/(?P<product_id>\d+)$', views.product_details, name='product_details'),
    url(r'^cart$', views.cart, name="cart"),
    url(r'^cart/(?P<product_id>\d+)/$', views.add_to_cart, name="add_to_cart"),
    url(r'^cart/remove/(?P<order_id>\d+)/$', views.remove_from_cart, name="remove_from_cart"),
    url(r'^categories$', views.categories, name="categories"),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name="profile"),
    url(r'^profile/(?P<pk>\d+)/add_payment_option$', views.add_payment, name="add_payment"),
    url(r'^profile/(?P<pk>\d+)/order_history$', views.order_history, name="order_history"),
    url(r'^profile/(?P<pk>\d+)/order_history/(?P<order_id>\d+)/$', views.order_history_details, name="order_history_details"),

]