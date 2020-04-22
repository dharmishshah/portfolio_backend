from portfolio.models.models import Education, Experience, Skills, Projects

def getAllEducations():
    educations = Education.objects.all()
    values = []
    for e in educations:
        values.append(e)
    return values

def getAllExperiences():
    educations = Experience.objects.all()
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
    educations = Projects.objects.all()
    values = []
    for e in educations:
        values.append(e)
    return values
