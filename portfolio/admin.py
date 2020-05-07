from django.contrib import admin

# Register your models here.
from portfolio.models.models import Education, Experience, Skills, Projects,Certificates, Recommendations, Personal, \
                                    Publications, BasicDetails

admin.site.register([Education, Experience, Skills, Projects , Certificates, Recommendations, Personal, Publications,
                     BasicDetails])
