import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'GitQuidProject.settings')
import django
django.setup()
from GitQuid.models import *


# Db setup:
# 1. python manage.py migrate
# 2. python manage.py makemigrations
# 3. python manage.py createsuperuser

def populate():
    d = add_Donation("None", 123.99, "12/12/2108", "Good project")
    p = add_Project(d, "Awesome project", "Lorem Ipsum of the awesome project"
                                      "Board games")
    add_Media(p, "picture0", 0)
    add_Media(p, "picture1", 1)

def add_Project(donation, name, body, category):
    p = Project.objects.get_or_create()
    p.donation = donation
    p.name = name
    p.body = body
    p.category = category
    p.save()
    return p

def add_User(name, password, email, pic, desc):
    u = UserProfile.objects.get_or_create()
    return u

def add_Media(project, tag, media):
    m = Media.objects.get_or_create()
    m.project = project
    m.tag = tag
    m.media = media
    m.save()
    return m

def add_Donation(user, amount, date, comment):
    d = Donation.objects.get_or_create()
    d.user = user
    d.amount = amount
    d.date = date
    d.comment = comment
    d.save()
    return d

if __name__ == '__main__':
    print("Populating...")
    populate()