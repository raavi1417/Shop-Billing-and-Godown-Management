"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('admin_part',admin_part),
    path('show',show),
    path('register',register),
    path('admin_login',admin_login),
    path('admin_logout',admin_logout),
    path('search',search),
    path('add_to_cart',add_to_cart,name='add_to_cart'),
    path('cart',cart_details,name='cart'),
    path('bill',Billing),
    path('delete_item_cart/<int:id>',delete_item_cart),
    path('clear_cart',delete_all),
    path('delete_item/<int:id>',delete_item),
    path('edit/<int:id>',edit),
    path('Data_update/<int:id>',Data_update),
    path('notifiaction',notification),
    path('stock',stock),
 
]
