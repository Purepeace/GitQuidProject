# TO-DO: add pictures and long text properly
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GitQuidProject.settings')
import django

django.setup()
from GitQuid.models import *
from django.utils import timezone
# plain text password are not stored in db only their hashes
from django.contrib.auth.hashers import make_password
import datetime


# Db setup:
# 0. if models were changed wipe db deleting all migrations from GitQuid/migrations (do NOT delete __init__.py) and
# deleting db file (flush is not enough)
# 1. python manage.py migrate (create default django model like user)
# 2. python manage.py makemigrations ("render" custom models)
# 3. python manage.py migrate (apply custom models)
# python manage.py createsuperuser
# Sauce: https://docs.djangoproject.com/en/2.0/intro/tutorial02/
# Display sql db? python manage.py sqlmigrate GitQuid 0001 (can't run if some django code doesn't compile)

# !!! python manage.py flush - to wipe db or you'll get errors if you are trying to repopulate existing db !!!


def populate():
    # User signs up
    u = User(username="Berta", password=make_password("password123XDXD"), email="hi@labas.lt", is_superuser=True,
             is_staff=True)
    u.save()
    # User sets up profile
    up = UserProfile(id=None, user=u, picture=None, description="Hi I am from Wilno")
    up.save()
    # User creates a project
    p = Project(userProfile=up, name="Awesome project", body="Lorem Ipsum of the awesome project",
                category="Board games")
    p.save()

    p2 = Project(userProfile=up, name="Awesome project2", body="Lorem Ipsum of the awesome project2",
                 category="Board games")
    p2.save()

    p3 = Project(userProfile=up, name="Awesome project3", body="Lorem Ipsum of the awesome project3",
                 category="ABoard games")
    p3.save()

    # User ads some pictures to the project
    Media(project=p, media=b"asdf", tag="picture0").save()
    Media(project=p, media=b"qwerty", tag="picture1").save()
    # User makes a donation and donation goes to a project
    d = Donation(userProfile=up, project=p, amount=123.99, date=timezone.now(), comment="Good project")
    d.save()
    d2 = Donation(userProfile=up, project=p2, amount=419.99, date=timezone.now(), comment="Awesome project")
    d2.save()
    d3 = Donation(userProfile=up, project=p3, amount=1337.00, date=timezone.now(), comment="Amazing project")
    d3.save()


#     u = add_User("Berta", "latushk", "hi@labas.lt", None, "Hi I am from Wilno")
#     d = add_Donation(u.id, 123.99, "2019-12-25T00:00:00-08:00", "Good project")
#     p = add_Project(d.id, "Awesome project", "Lorem Ipsum of the awesome project"
#                                              "Board games")
#     add_Media(p, "picture0", 0)
#     add_Media(p, "picture1", 1)
#
#
# def add_Project(donation, name, body, category):
#     p = Project.objects.get_or_create()
#     p.donation = donation
#     p.name = name
#     p.body = body
#     p.category = category
#     p.save()
#     return p
#
#
# def add_User(name, u_password, email, pic, u_desc):
#     us = User.objects.get_or_create(username=name, password=u_password)[0]
#     us.email = email
#     us.save()
#     u = UserProfile.objects.get_or_create(user=us, description=u_desc)
#     return u
#
#
# def add_Media(project, tag, media):
#     m = Media.objects.get_or_create()
#     m.project = project
#     m.tag = tag
#     m.media = media
#     m.save()
#     return m
#
#
# def add_Donation(d_user, d_amount, d_date, comment):
#     d = Donation.objects.get_or_create(amount=d_amount, date=d_date, user=d_user)
#     d.comment = comment
#     d.save()
#     return d


if __name__ == '__main__':
    print("Populating...")
    populate()
