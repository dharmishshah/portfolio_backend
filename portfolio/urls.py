from django.urls import path
from . import views

urlpatterns = [
    path('home1', views.indexHome, name='indexHome'),
    path('', views.index, name='index'),
    path('jsonHome',views.indexHomeJson,name='id')
]