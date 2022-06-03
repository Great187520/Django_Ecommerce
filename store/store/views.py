from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/Store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/Cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #Create Empty cart for now none-loggoed in users
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []

    context = {'items': items, 'order':order}

    context = {}
    return render(request, 'store/Checkout.html', context)
