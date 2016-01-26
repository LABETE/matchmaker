from django.shortcuts import render
from django.views.generic.detail import DetailView

from profiles.models import UserJob
from .models import Job, Location, Employer


class JobDetailView(DetailView):
    model = Job

    def get_context_data(self, *args, **kwargs):
        context = super(JobDetailView, self).get_context_data(*args, **kwargs)
        print(kwargs["object"].name)
        users = UserJob.objects.filter(position__iexact=kwargs["object"].name).exclude(user=self.request.user)
        context["users"] = users
        return context


class LocationDetailView(DetailView):
    model = Location

    def get_context_data(self, *args, **kwargs):
        context = super(LocationDetailView, self).get_context_data(*args, **kwargs)
        users = UserJob.objects.filter(location__iexact=kwargs["object"].name).exclude(user=self.request.user)
        context["users"] = users
        return context


class EmployerDetailView(DetailView):
    model = Employer

    def get_context_data(self, *args, **kwargs):
        context = super(EmployerDetailView, self).get_context_data(*args, **kwargs)
        users = UserJob.objects.filter(employer__iexact=kwargs["object"].name).exclude(user=self.request.user)
        context["users"] = users
        return context
