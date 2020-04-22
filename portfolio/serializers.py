from django.contrib.auth.models import User, Group
from rest_framework import serializers
from portfolio.models.models import Education


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ['name','city' ,'state','state_abbr', 'country', 'country_abbr', 'fromYear', 'toYear', 'gpa' ,
                  'degree', 'major', 'status','imageLink','course']