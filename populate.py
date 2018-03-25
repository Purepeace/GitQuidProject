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


loremWithMarkdown = """# Daulida bis non grave fecerit margine Diomede

## Gramineo mortale praestantes sinus Delon altior ponitque

Lorem markdownum naufraga o vitae meo mutatus cuspide sine breviter quisque
confisa repugnat aethere; qui mearum nefas: alis. Glaebaque Naxon non Parosque
utve, quam [manu imbres](http://pietas-dea.io/loranymphae.php) pudor, Asopidos,
a. Plangore cuspidis cogis boum id *nihil succedit*, aetas pulmonis labores
aestu adsumere adpositis! Radice toto torum, pontus alii, nec pars ferus,
iuvenem prohibete modo oculis dare iuventae latet.

1. Cum hinc stipite locuta
2. Fulmen desierant sacro tale o venit comitavit
3. Loqui viridesque madefacta plenis
4. Ceu ab Alcidamas victa nemorum recanduit quae

Capax desertum si **tellus concretam** posses thalamoque, ipse qua. In adiectura
sanguis Argus Phrygum Athon. Auctor lassaque collesque partem, tot vix asper
maduere inaniter, vestem usu defluxere quae nec nomen? Urbe ultima de requiret
suo fores vertisse frutices inplet capillos capillos.

## Nurusque finis

In enim, qua materna silva longa huius fauces, captam ad, in. Cum non frontis
idonea tristes inpresso moras. Hastam et simul armatus!

Petis quot; *tamen invergens* ingentique, aera repandus quales: nomen omnibus.
Balatum et lacrimosa pereunt haec, Sol, ne vestri creatos Aethalion hunc tenuere
arbitrio Aonios transformia. Oleis hastamque Aegaeas inde; lac res sanguine
adhuc reperire. Est dixit dolores, at animam antro pectora crescente cadunt!

> Aeolon in positaeque Thessalidum nodoso freta. Pomaria alta matris ad extimuit
> addit!

Adsuerant daedalus insilit belua creatam saltus ut vultus, me fuit suarum priori
[vaga negare](http://iuvencumpraecepta.io/) est artem toto est. Matutina
plurimus arte habitabilis suae pectora septem saeva commota, sibi.

Radiis repagula ramis est: et sertaque, postque silices fuit tibi
[non](http://nisi-proavitaque.io/dedit-pictasque)! Exactum mundi quae borean,
pictis Oceani fictamque, non alto sua et herbis, nostra ni potestas."""

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
    p = Project(user=u, name="Awesome project", body=loremWithMarkdown,
                category=c, date=datetime.datetime(2015, 12, 1, 23, 59))
    p.save()

    p2 = Project(user=u, name="Wonderful project", body="We need money",
                 category=c2, date=datetime.datetime(2019, 12, 1, 23, 59))
    p2.save()

    p3 = Project(user=u, name="Decent project", body="Please donate",
                 category=c3, date=datetime.datetime(2012, 12, 1, 23, 59))
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
