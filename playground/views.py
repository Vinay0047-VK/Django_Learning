from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order
# Create your views here.

def say_hello(request):
    
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]

    return render(request,'hello.html',{'name':'Vinay', 'orders':list(query_set)})