from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is the Music app homepage.</h1> Hello again!")

def detail(request, album_id):
    return HttpResponse("<h1>Details for album id:" + str(album_id) + "</h1>")
