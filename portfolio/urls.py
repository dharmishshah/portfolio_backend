from django.urls import path
from . import views

from django.conf.urls import url, include
from rest_framework import routers
from portfolio import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'educations', views.EducationViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('getEducations',views.getAllEducations,name='getAllEducations'),
    path('getExperiences',views.getAllExperiences,name='getAllExperiences'),
    path('getSkills',views.getAllSkills,name='getAllSkills'),
    path('getProjects',views.getAllProjects,name='getAllProjects'),
    path('getCertificates',views.getAllCertificates,name='getAllCertificates'),
    path('getRecommendations',views.getAllRecommendations,name='getAllRecommendations'),
    path('getPersonalInfo',views.getAllPersonalInfo,name='getAllPersonalInfo'),
    path('sendEmail',views.sendEmail,name='sendEmail'),

    path('', include(router.urls)),

]