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
    u = add_User("Berta","latushk","hi@labas.lt",None,"Hi I am from Wilno")
    d = add_Donation(u, 123.99, "2019-12-25T00:00:00-08:00", "Good project")
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

def add_User(name, u_password, email, pic, u_desc):
    us = User.objects.get_or_create(username=name, password=u_password)[0]
    us.email = email
    us.save()
    u = UserProfile.objects.get_or_create(user=us,description = u_desc)
    return u

def add_Media(project, tag, media):
    m = Media.objects.get_or_create()
    m.project = project
    m.tag = tag
    m.media = media
    m.save()
    return m

def add_Donation(d_user, d_amount, d_date, comment):
    d = Donation.objects.get_or_create(amount=d_amount,date=d_date,user=d_user)
    d.comment = comment
    d.save()
    return d

if __name__ == '__main__':
    print("Populating...")
    populate()
