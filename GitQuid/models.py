from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Django creates primary key automatically if not specified btw
# on_delete=models.PROTECT - Django 2.0 requires that


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    picture = models.BinaryField(blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.user.username

class Donation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    amount = models.FloatField(blank=True)
    date = models.DateTimeField(blank=True)
    comMaxLen = 200
    comment = models.CharField(max_length=comMaxLen, blank=True)

class Project(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

# Table to store whatever material was uploaded to the project (picture, vids, etc.)
# Many-to-one relation with project
class Media(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    tag = models.CharField(max_length=50, blank=True)
    media = models.BinaryField(blank=True)
