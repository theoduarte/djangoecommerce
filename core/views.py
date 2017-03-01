# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

#from catalog.models import Category
from .forms import ContactForm
import pprint

# Create your views here.

def index(request):
    
    texts = ['desenvolvendo com Django Python', ' com curso Udemy']
    context = {
        'title': 'django E-Commerce',
        'texts': texts
        #'categories': Category.objects.all()
    }
    
    return render(request, 'index.html', context)

def contact(request):
    
    form = ContactForm(request.POST or None)

    success = False

    if form.is_valid():
        form.send_mail()
        success = True
    
    context = {
        'form': form,
        'success': success
    }
    
#    pprint.isrecursive(form)
#    pprint.pprint(form, depth=4)
#    pprint.pprint(form.as_p)
#    {{ form.as_p }}
    
    
    return render(request, 'contact.html', context)

def product(request):
    return render(request, 'product.html')

#def product_list(request):
#    return render(request, 'product_list.html')

