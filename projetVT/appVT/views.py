from django.shortcuts import render
from django.http import HttpResponse
from .models import movies
# Create your views here.

def index(response):
    return render(response, "index.html")

def data(response, id):
    ls = movies.objects.get(id=id)
    return HttpResponse("<h1>%s</h1" %ls.title)