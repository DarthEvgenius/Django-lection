from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def jekka(request):
    return HttpResponse("Hello, Jekka")


def cs50(request):
    return HttpResponse("Hello, cs50")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
