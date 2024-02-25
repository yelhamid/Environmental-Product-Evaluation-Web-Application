from ast import Return
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'base/home.html')

def about(request):
    return render(request,'pages/about.html')
