from djongo import models

class Education(models.Model):
    id == models.GenericObjectIdField
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
    status = models.CharField(max_length=100)
    course = models.ArrayField

    def __str__(self):
        return "education"