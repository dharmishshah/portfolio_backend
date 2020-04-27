from datetime import datetime
from django.core.mail import send_mail

from Portfolio_backend.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT
from portfolio.models.models import Education, Experience, Skills, Projects, Certificates, Recommendations, \
    Personal, EmailDetails, Publications



def getAllEducations():
    educations = Education.objects.all().order_by("-dateFormat")
    values = []
    for e in educations:
        values.append(e)
    return values

def getAllExperiences():
    educations = Experience.objects.all().order_by("-dateFormat")
    values = []
    for e in educations:
        values.append(e)
    return values

def getAllSkills():
    educations = Skills.objects.all()
    values = []
    for e in educations:
        values.append(e)
    return values

def getAllProjects():
    educations = Projects.objects.all().order_by("-dateFormat")
    values = []
    for e in educations:
        values.append(e)
    return values

def getAllCertificates():
    certificates = Certificates.objects.all().order_by("-dateFormat")
    values = []
    for e in certificates:
        values.append(e)
    return values

def getAllRecommendations():
    recommendations = Recommendations.objects.all().order_by("-dateFormat")
    values = []
    for e in recommendations:
        values.append(e)
    return values

def getAllPersonalInfo():
    personal = Personal.objects.all()
    values = []
    for e in personal:
        values.append(e)
    return values


def getAllPublications():
    publication = Publications.objects.all().order_by("-dateFormat")
    values = []
    for e in publication:
        values.append(e)
    return values

def sendEmail(name, organisation, email, message):
    e = EmailDetails()
    e.email = email
    e.name = name
    e.date = datetime.now()
    e.organisation = organisation
    e.message = message
    e.save()
    subject = "New Mail from Portfolio"
    smessage = name + ", " + organisation + ", " + email + " ------------- " + message
    send_mail(subject, smessage, EMAIL_HOST_USER,[EMAIL_RECIPIENT], fail_silently = False)
