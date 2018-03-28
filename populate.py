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
    up = UserProfile(user=u, picture=None, description="Hello i am the superuser")
    up.save()

    # Create categories
    c = Category(name="Art", views="100", likes="16")
    c.save()
    c2 = Category(name="Comics", views="201", likes="26")
    c2.save()
    c3 = Category(name="Crafts", views="100", likes="16")
    c3.save()
    c4 = Category(name="Dance", views="100", likes="16")
    c4.save()
    c5 = Category(name="Design", views="201", likes="26")
    c5.save()
    c6 = Category(name="Fashion", views="100", likes="16")
    c6.save()
    c7 = Category(name="Film & Video", views="100", likes="16")
    c7.save()
    c8 = Category(name="Food", views="201", likes="26")
    c8.save()
    c9 = Category(name="Games", views="100", likes="16")
    c9.save()
    c10 = Category(name="Journalism", views="100", likes="16")
    c10.save()
    c11 = Category(name="Music", views="50", likes="5")
    c11.save()
    c12 = Category(name="Photography", views="100", likes="16")
    c12.save()
    c13 = Category(name="Publishing", views="100", likes="16")
    c13.save()
    c14 = Category(name="Technology", views="201", likes="26")
    c14.save()
    c15 = Category(name="Theatre", views="100", likes="16")
    c15.save()

    # User creates a project
    p = Project(user=u, name="Awesome project", body="Money for charity",
                category=c,  dateCreated=datetime.datetime(2015, 12, 1, 23, 59))
    p.save()

    p2 = Project(user=u, name="Wonderful project", body="We need money",
                 category=c2, dateCreated=datetime.datetime(2019, 12, 1, 23, 59))
    p2.save()

    p3 = Project(user=u, name="Decent project", body="Please donate",
                 category=c3, dateCreated=datetime.datetime(2012, 12, 1, 23, 59))
    p3.save()

    # User makes a donation and donation goes to a project
    d = Donation(user=u, project=p, amount=123.99, date=timezone.now(), comment="Good project")
    d.save()
    d2 = Donation(user=u, project=p2, amount=419.99, date=timezone.now(), comment="Awesome project")
    d2.save()
    d3 = Donation(user=u, project=p3, amount=1337.00, date=timezone.now(), comment="Amazing project")
    d3.save()



if __name__ == '__main__':
    print("Populating...")
    populate()
