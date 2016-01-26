from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from likes.models import Like
from matches.models import Match
from .forms import UserJobFormSet, UserJobForm, UserProfileForm
from .models import Profile, UserJob


class UserJobUpdateView(ListView):
    model = UserJob

    def get_context_data(self, *args, **kwargs):
        context = super(UserJobUpdateView, self).get_context_data(
            *args, **kwargs)
        context["formset"] = UserJobFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        return self.request.user.userjob_set.all()

    def post(self, *args, **kwargs):
        formset = UserJobFormSet(self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = self.request.user
                instance.save()
            slug = self.request.user.profile.slug
            messages.success(self.request, 'Your jobs were updated successfuly.', extra_tags="success")
            return redirect(self.request.user.profile.get_absolute_url(), kwargs={"slug": slug})
        messages.error(self.request, 'An error occured, try again.', extra_tags="error")
        return redirect("profiles:update")


class UserJobCreateView(CreateView):
    model = UserJob
    form_class = UserJobForm

    def post(self, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            add_job = form.save(commit=False)
            add_job.user = self.request.user
            add_job.save()
            messages.success(self.request, 'Your jobs was added successfuly.', extra_tags="success")
            slug = self.request.user.profile.slug
            return redirect(self.request.user.profile.get_absolute_url(), kwargs={"slug": slug})
        messages.error(self.request, 'An error occured, try again.', extra_tags="error")
        return redirect("profiles:create")


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(
            *args, **kwargs)
        User = get_user_model()
        user_b = get_object_or_404(User, username=kwargs["object"])
        user_like, user_like_created = Like.objects.get_or_create(
            user=self.request.user)
        mutual_like = user_like.get_mutual_like(user_b)
        do_i_like = False
        if user_b in user_like.liked_users.all():
            do_i_like = True
        match = Match.objects.get_or_create_match(
            user_a=self.request.user, user_b=user_b)[0]
        jobs = self.request.user.userjob_set.all()
        if match:
            context["match_percent"] = match.match_percent
        context["jobs"] = jobs
        context["mutual_like"] = mutual_like
        context["do_i_like"] = do_i_like
        return context


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/my_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(
            *args, **kwargs)
        context["jobs"] = self.request.user.userjob_set.all()
        context["user_not_allowed"] = "You are not allowed to view this page"
        return context


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Your profile was updated successfuly.', extra_tags="success")
        return super(UpdateProfile, self).form_valid(form)
