from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    lst = list(range(6,15))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    return render(request, 'generator/password.html')