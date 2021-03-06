from datetime import datetime
from django.db import models
from django.utils import timezone


class Education(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    state_abbr = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_abbr = models.CharField(max_length=100)
    fromYear = models.CharField(max_length=100)
    toYear = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    imageLink = models.CharField(max_length=200)
    courses = models.CharField(max_length=1000)
    link = models.CharField(max_length=200)
    dateFormat = models.DateField()
    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    state_abbr = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_abbr = models.CharField(max_length=100)
    fromYear = models.CharField(max_length=200)
    toYear = models.CharField(max_length=200)
    techStack = models.CharField(max_length=1000)
    status = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    dateFormat = models.DateField()


    def __str__(self):
        return self.company

class Skills(models.Model):
    languages = models.CharField(max_length=1000)
    backend = models.CharField(max_length=1000)
    frontend = models.CharField(max_length=1000)
    databases = models.CharField(max_length=1000)
    libraries = models.CharField(max_length=1000)
    development = models.CharField(max_length=1000)
    def __str__(self):
        return self.languages

class Projects(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    state_abbr = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_abbr = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    techStack = models.CharField(max_length=1000)
    link = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=200)
    githubBackend = models.CharField(max_length=200)
    githubFrontend = models.CharField(max_length=200)
    status = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    dateFormat = models.DateField()
    def __str__(self):
        return self.name

class Certificates(models.Model):
    name = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)
    expiryDate = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    status = models.CharField(max_length=1000)
    dateFormat = models.DateField()
    def __str__(self):
        return self.name

class Publications(models.Model):
    name = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)
    expiryDate = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    status = models.CharField(max_length=1000)
    dateFormat = models.DateField()

    def __str__(self):
        return self.name

class Recommendations(models.Model):
    name = models.CharField(max_length=1000)
    organisation = models.CharField(max_length=1000)
    role = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)
    linkedInlink = models.CharField(max_length=200)
    imageLink = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    status = models.CharField(max_length=1000)
    dateFormat = models.DateField()

    def __str__(self):
        return self.name

class Personal(models.Model):
    interests = models.CharField(max_length=10000)
    honors =  models.CharField(max_length=10000)
    achievements =  models.CharField(max_length=10000)
    imageLink = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    status = models.CharField(max_length=1000)
    dateFormat = models.DateField()

    def __str__(self):
        return self.interests

class EmailDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    organisation = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.email


class BasicDetails(models.Model):
    name = models.CharField(max_length=100)
    about1 = models.CharField(max_length=10000)
    about2 = models.CharField(max_length=10000)
    role = models.CharField(max_length=1000)
    resumeLink = models.CharField(max_length=1000)
    email = models.CharField(max_length=100)
    github = models.CharField(max_length=1000)
    linkedin = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=1000)

    def __str__(self):
        return self.name