# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

#from catalog.models import Category
from .forms import ContactForm
import pprint


User = get_user_model()
# Create your views here.

class IndexView(View):

#    def __call__(self, request):
#
#        texts = ['desenvolvendo com Django Python', ' com curso Udemy']
#        context = {
#            'title': 'django E-Commerce',
#            'texts': texts
#            #'categories': Category.objects.all()
#        }
#
#        return render(request, 'index.html', context)

    def get(self, request):

        texts = ['desenvolvendo com Django Python', ' com curso Udemy']
        context = {
            'title': 'django E-Commerce',
            'texts': texts
            #'categories': Category.objects.all()
        }

        return render(request, 'index.html', context)

#index = IndexView()
index = IndexView.as_view()

def index(request):

    texts = ['desenvolvendo com Django Python', ' com curso Udemy', ' e melhorando as views']
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

# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     model = User
#     success_url = reverse_lazy('index')
#
# register = RegisterView.as_view()
