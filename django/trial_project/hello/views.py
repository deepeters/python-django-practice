from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world!")

def index(request):
    return render(request, "hello/index.html")

def dennis(request):
    return HttpResponse("Hello, Dennis!")

def esther(request):
    return HttpResponse("Hello, Esther!")

def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })