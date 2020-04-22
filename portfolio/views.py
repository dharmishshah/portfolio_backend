from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import portfolio.manager.manager as e

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from portfolio.models.models import Education
from portfolio.serializers import UserSerializer, GroupSerializer, EducationSerializer

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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]