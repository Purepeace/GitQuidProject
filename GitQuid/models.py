from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


# Django creates primary key automatically if not specified btw
# on_delete=models.PROTECT - Django 2.0 requires that

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):  # For Python 2, use__unicode__ too
        return self.name


class UserProfile(models.Model):
    # what happens if user wants to delete his profile?
    # models.PROTECT will preserve data in the db which imo shouldn't be the case
    # However, projects and donation history should be preserved
    # Anyhow, not a primary concern
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    # ideally maybe many users (as a team, for instance) could create a many projects
    # but keeping one user creates many projects is a bit simpler for now
    userProfile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now())
    description = models.CharField(max_length=300, null=True)
    title_image = models.ImageField(upload_to="title_images", null=True, blank=True)
    body = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # for internal use only. Sum of all donations to this project
    donations = models.FloatField(default=0)


    def __str__(self):
        return self.name


class Donation(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now())
    comMaxLen = 200
    comment = models.CharField(max_length=comMaxLen, null=True)

    def __str__(self):
        return str(self.amount) + ' to ' + str(self.project) + ' at ' + str(self.date)[:16]


# Table to store whatever material was uploaded to the project (picture, vids, etc.)
# Many-to-one relation with project
class Media(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    media = models.BinaryField()

    def __str__(self):
        return self.tag
