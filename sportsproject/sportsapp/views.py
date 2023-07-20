from urllib import request

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "intex.html")


def addition(request):
    return render(request, "result.html")


x = int(request.GET['num1'])
y = int(request.GET['num2'])
res = x + y
result.render(request, "result.html", {'result': res})
