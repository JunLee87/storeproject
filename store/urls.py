from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^products/$', views.products, name='products'),
    re_path(r'^tags/$', views.tags, name='tags'),
    re_path(r'^detail/$', views.detail, name='detail'),
    re_path(r'^register/$', views.do_reg, name='register'),
    re_path(r'^login/$', views.do_login, name='login'),
    re_path(r'^logout/$', views.do_logout, name='logout'),
    re_path(r'^view_cart/$', views.view_cart, name='view_cart'),
    re_path(r'^add_cart/$', views.add_cart, name='add_cart'),
    re_path(r'^view_order/$', views.view_order, name='view_order'),
    re_path(r'^clean_cart/$', views.cleanCart, name='clean_cart'),
    re_path(r'^brands/$', views.brands, name='brands'),
    re_path(r'discount/$', views.getDiscount, name='discount'),
]
