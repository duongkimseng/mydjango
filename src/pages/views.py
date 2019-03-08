from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip


def homepage(request, *args, **kwargs):
    return render(request, 'home.html', {})

def productspage(request, *args, **kwargs):
    return render(request, 'products.html', {})

def contactpage(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def aboutpage(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": '001829485',
        "my_list": ["facebook","youtube","google","microsoft"]
    }
    return render(request, 'about.html', my_context)