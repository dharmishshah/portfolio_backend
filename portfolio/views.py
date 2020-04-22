from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import portfolio.manager.manager as e

def index(request):
    return HttpResponse("Hello, world. You're at the portfolio index.")

def getAllEducations(request):
    edu = e.getAllEducations()
    edu_json = serializers.serialize('json', edu)
    return HttpResponse({edu_json})

def getAllExperiences(request):
    edu = e.getAllExperiences()
    edu_json = serializers.serialize('json', edu)
    return HttpResponse({edu_json})

def getAllSkills(request):
    edu = e.getAllSkills()
    edu_json = serializers.serialize('json', edu)
    return HttpResponse({edu_json})

def getAllProjects(request):
    edu = e.getAllProjects()
    edu_json = serializers.serialize('json', edu)
    return HttpResponse({edu_json})
