from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
        #html = "<!DOCTYPE html><html><a href='/rango/about/'>About</a></html>"
        return HttpResponse("Rango says hey there!" + "<a href='/rango/about/'>About</a>")


def about(request):
        return HttpResponse("Rango says this is the about page!" + "<a href = '/rango'>Index</a>")
