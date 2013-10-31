#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def anotherPage(request):
    return HttpResponse("Hello, world. You're at more.")

def detail(request, poll_id):
    return HttpResponse