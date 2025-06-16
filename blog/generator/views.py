
import random
from django.shortcuts import render
from django.http import HttpResponse
from random import choice




def home(request):
    lst = list(range(6,15))
    return render(request, 'generator/home.html', {'lst': lst})


import random
from django.shortcuts import render

def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    char = [chr(i) for i in range(97, 123)]


    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('number'):
        char.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])




    length = int(request.GET.get('len', 12))


    psw = ''
    for i in range(length):
        psw+=random.choice(char)

    return render(request, 'generator/password.html', {'password': psw})
