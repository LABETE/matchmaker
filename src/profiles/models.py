from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from jobs.models import Location, Job, Employer


def upload_location(instance, filename):
    location = str(instance.user.username)
    return "{0}/{1}".format(location, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    slug = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("profiles:my_profile", kwargs={"slug": self.slug})

    def like_link(self):
        return reverse("like:detail", kwargs={"pk": self.user.pk})


def pre_save_profile_slug_receiver(sender, instance, *args, **kwargs):
    username_slug = slugify(instance.user.username)
    instance.slug = username_slug

pre_save.connect(pre_save_profile_slug_receiver, sender=Profile)


class UserJob(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    position = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    employer = models.CharField(max_length=220)

    def __str__(self):
        return self.position


def pre_save_user_job(sender, instance, *args, **kwargs):
    job = instance.position.lower()
    location = instance.location.lower()
    employer_name = instance.employer.lower()
    new_job = Job.objects.get_or_create(name=job)
    new_location = Location.objects.get_or_create(name=location)[0]
    new_employer = Employer.objects.get_or_create(location=new_location, name=employer_name)

pre_save.connect(pre_save_user_job, sender=UserJob)

