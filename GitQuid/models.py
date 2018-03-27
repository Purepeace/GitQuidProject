from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.urls import reverse
import itertools


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
    slug = models.SlugField(unique=True, null=True)

    # ensures unique slug (concat with id in case there are similar username which only differ by lower/upper cases)
    def save(self, *args, **kwargs):
        # this is good enough as changing username is not allowed, therefore, the slug will be constant
        # and urls won't break
        self.slug = slugify(''.join([str(self.user.username), '-', str(self.user.id)]))
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    # ideally maybe many users (as a team, for instance) could create a many projects
    # but keeping one user creates many projects is a bit simpler for now

    # null=True shouldn't be here. Something is broken with user detection in add_project view
    # userProfile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    maxLen = 200
    name = models.CharField(max_length=maxLen)
    # __current_name = None
    slug = models.SlugField(max_length=(maxLen + 50), unique=True, null=True)
    date = models.DateTimeField(default=timezone.now())
    description = models.CharField(max_length=maxLen, blank=True, default='')
    title_image = models.ImageField(upload_to='title_images', blank=True)
    body = MarkdownxField(blank=True, default='')
    published = models.BooleanField(default=False)
    # change
    goal = models.FloatField(default=-69)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # for internal use only. Sum of all donations to this project
    donations = models.FloatField(default=0, blank=True)

    # def __init__(self, *args, **kwargs):
    #     super(Project, self).__init__(*args, **kwargs)
    #     self.__current_name = self.name

    # ensures unique slug. Slug is changed if project name is changed
    def save(self, *args, **kwargs):
        # if model was just created
        # Sauce: https://stackoverflow.com/questions/2307943/django-overriding-the-model-create-method
        print(self.id)
        if self.id is None:
            # save to make sure that project has id
            super(Project, self).save(*args, **kwargs)
        self.slug = slugify(''.join([self.name, "-", str(self.id)]))
        super(Project, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    @property
    def formatted_markdown(self):
        return markdownify(self.body)


class Donation(models.Model):
    userProfile = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now())
    comMaxLen = 200
    comment = models.CharField(max_length=comMaxLen, blank=True, default='')

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
