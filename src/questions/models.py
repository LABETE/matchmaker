from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save


class QuestionManager(models.Manager):

    def get_unanswered_questions(self, user):
        answered_questions = user.useranswer_set.all().values_list("question")
        return self.exclude(pk__in=answered_questions)


class Question(models.Model):
    text = models.TextField()
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    objects = QuestionManager()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.text

LEVELS = (
    ('Mandatory', 'Mandatory'),
    ('Very Important', 'Very Important'),
    ('Somewhat Important', 'Somewhat Important'),
    ('Not Important', 'Not Important'),
)


class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    my_answer = models.ForeignKey(Answer, related_name='user_answer')
    my_points = models.IntegerField(default=-1)
    my_answer_importance = models.CharField(max_length=50, choices=LEVELS)
    their_answer = models.ForeignKey(Answer, null=True, blank=True, related_name='match_answer')
    their_points = models.IntegerField(default=-1)
    their_importance = models.CharField(max_length=50, choices=LEVELS)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.question)


def points_pre_save_receiver(sender, instance, *args, **kwargs):
    my_points = get_points(instance.my_answer_importance)
    their_points = get_points(instance.their_importance)
    instance.my_points = my_points
    instance.their_points = their_points

pre_save.connect(points_pre_save_receiver, sender=UserAnswer)


def get_points(importance):

    if importance == "Mandatory":
        points = 500
    elif importance == "Very Important":
        points = 300
    elif importance == "Somewhat Important":
        points = 100
    elif importance == "Not Important":
        points = 0
    return points
