from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the portfolio index.")

def indexHome(request):
    return HttpResponse("Hello, world. ")

def indexHomeJson(request):
    return JsonResponse({"message":"Hello"})
