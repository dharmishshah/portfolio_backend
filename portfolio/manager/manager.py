from portfolio.models.models import Education

def getAllEducations():
    educations = Education.objects.all()
    values = []
    for e in educations:
        values.append(e)

    return values
