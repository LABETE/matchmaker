from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Job(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.CharField(max_length=220, unique=True)
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.name


def pre_save_job_slug(sender, instance, *args, **kwargs):
    slug_name = slugify(instance.name)
    instance.slug = slug_name


pre_save.connect(pre_save_job_slug, sender=Job)


class Location(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.CharField(max_length=220, unique=True)
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.name


def pre_save_location_slug(sender, instance, *args, **kwargs):
    slug_name = slugify(instance.name)
    instance.slug = slug_name


pre_save.connect(pre_save_location_slug, sender=Location)


class Employer(models.Model):
    name = models.CharField(max_length=220)
    slug = models.CharField(max_length=220, unique=True)
    location = models.ForeignKey(Location, null=True, blank=True)

    def __str__(self):
        return self.name


def pre_save_employer_slug(sender, instance, *args, **kwargs):
    try:
        Employer.objects.get(slug=slugify(instance.name))
    except:
        slug_name = slugify(instance.name)
        instance.slug = slug_name


pre_save.connect(pre_save_employer_slug, sender=Employer)


class PositionMatch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    job = models.ForeignKey(Job)
    hidden = models.BooleanField(default=False)
    liked = models.NullBooleanField()

    def __str__(self):
        return str(self.user.username)


class LocationMatch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    location = models.ForeignKey(Location)
    hidden = models.BooleanField(default=False)
    liked = models.NullBooleanField()

    def __str__(self):
        return str(self.user.username)


class EmployerMatch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    employer = models.ForeignKey(Employer)
    hidden = models.BooleanField(default=False)
    liked = models.NullBooleanField()

    def __str__(self):
        return str(self.user.username)
