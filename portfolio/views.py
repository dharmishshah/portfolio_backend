from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the portfolio index.")

def indexHome(request):
    return HttpResponse("Hello, world. ")
