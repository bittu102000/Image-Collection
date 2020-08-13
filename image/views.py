from django.shortcuts import render, redirect
from .models import *


def home(request):
    cats = Categories.objects.all()
    image = Image.objects.all()
    data = {'image':image,'cats':cats}
    return render(request,"image/home.html",data)


def category(request,id):
    cats = Categories.objects.all()
    category = Categories.objects.get(pk=id)
    image = Image.objects.filter(cate=category)
    data = {'image':image,'cats':cats}
    return render(request,"image/home.html",data)
