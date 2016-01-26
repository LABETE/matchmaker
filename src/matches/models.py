import datetime

from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.dispatch import receiver
from django.utils import timezone

from profiles.models import Profile
from questions.signals import match
from .utils import get_match


@receiver(user_logged_in)
def get_user_matches_receiver(sender, request, user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)
    User = get_user_model()
    questions = user.useranswer_set.all()
    if questions:
        users = User.objects.all().order_by("?").exclude(username=user)[:200]
        for user_b in users:
            Match.objects.get_or_create_match(user, user_b)


class MatchQuerySet(models.query.QuerySet):

    def match_all(self, user):
        matches = []
        users = []
        match_a = self.filter(user_a=user)
        match_b = self.filter(user_b=user)
        match_set = (match_a | match_b).order_by("-match_decimal")
        for match in match_set:
            if match.user_a == user:
                users.append(match.user_b)
                items_wanted = [match.user_b, match.match_percent]
                matches.append(items_wanted)
            elif match.user_b == user:
                users.append(match.user_a)
                items_wanted = [match.user_a, match.match_percent]
                matches.append(items_wanted)
        return matches, users


class MatchManager(models.Manager):

    def get_queryset(self):
        return MatchQuerySet(self.model, using=self._db)

    def get_or_create_match(self, user_a=None, user_b=None):
        user_a_questions = user_a.useranswer_set.all()
        user_b_questions = user_b.useranswer_set.all()
        if user_a != user_b and user_a_questions and user_b_questions:
            try:
                match = self.get(user_a=user_a, user_b=user_b)
                match.check_update()
                created = False
            except Match.DoesNotExist:
                try:
                    match = self.get(user_a=user_b, user_b=user_a)
                    match.check_update()
                    created = False
                except Match.DoesNotExist:
                    match = self.create(user_a=user_a, user_b=user_b)
                    match.check_update()
                    created = True
            return match, created
        return False, False

    def get_match_all(self, user):
        return self.get_queryset().match_all(user)


class Match(models.Model):
    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
    match_decimal = models.DecimalField(max_digits=16, decimal_places=8, default=0.00)
    questions_answered = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = MatchManager()

    def __str__(self):
        return str(self.match_decimal)

    @property
    def match_percent(self):
        percent = "{0:.2f}%".format(self.match_decimal * 100)
        return percent

    def do_match(self):
        user_a = self.user_a
        user_b = self.user_b
        match_decimal, questions_answered = get_match(user_a, user_b)
        if match_decimal:
            self.match_decimal = match_decimal
            self.questions_answered = questions_answered
            self.save()

    def check_update(self):
        now = timezone.now()
        offset = now - datetime.timedelta(hours=12)
        if self.updated <= offset:
            self.do_match()


def do_match_receiver(sender, user, *args, **kwargs):
    User = get_user_model()
    users = User.objects.all().order_by("?").exclude(username=user)[:10]
    for user_b in users:
        Match.objects.get_or_create_match(user, user_b)


match.connect(do_match_receiver, sender=Match)
