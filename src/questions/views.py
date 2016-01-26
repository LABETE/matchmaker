from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import ModelFormMixin

from .mixins import PostQuestionMixin
from .models import Answer, Question, UserAnswer, LEVELS
from .forms import QuestionForm


class QuestionDetailView(PostQuestionMixin, ModelFormMixin, DetailView):
    model = Question
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context["answers"] = UserAnswer.objects.filter(
            user=self.request.user,
            question=self.object).first()
        context["levels"] = LEVELS
        context["form"] = self.form_class
        return context
