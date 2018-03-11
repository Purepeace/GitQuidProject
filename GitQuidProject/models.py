# Povilas

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User




class Project(models.Model):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class Donation(models.Model):
    user = models.OneToOneField(UserProfile)
