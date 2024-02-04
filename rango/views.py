from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
        # From TWD: Construct a dictionary to pass to the template engine as its context
        # Note the key boldmessage matches to {{ boldmessage }} in the template
        context_dict = {"boldmessage" : "Crunchy, creamy, cookie, candy, cupcake!"}

        # From TWD: Return a rendered response to send to the client
        # We make use of the shortcut funciton to make thigs easier
        # not ethat the first parameter is the template we want to use 
        return render(request, "rango/index.html", context = context_dict)


def about(request):
        context_dict = {"boldmessage" : "This tutorial was put together by Adam Harvey"}

        return render(request, "rango/about.html", context = context_dict)
        #return HttpResponse("Rango says this is the about page!" + "<a href = '/rango'>Index</a>")
