from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    # url('products', views.list_products, name='list_products'),
    url(r'^products/(?P<product_id>\d+)$', views.product_details, name='product_details'),
    url(r'^cart/(?P<pk>\d+)/$', views.cart, name="cart"),
    url(r'^categories$', views.categories, name="categories"),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name="profile"),
    url(r'^profile/(?P<pk>\d+)/add_payment_option$', views.add_payment, name="add_payment")

]