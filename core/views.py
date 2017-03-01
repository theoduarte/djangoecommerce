# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category

# Create your views here.

def index(request):
    
    texts = ['desenvolvendo com Django Python', ' com curso Udemy']
    context = {
        'title': 'django E-Commerce',
        'texts': texts,
        'categories': Category.objects.all()
    }
    
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

#def product_list(request):
#    return render(request, 'product_list.html')

