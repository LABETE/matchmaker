from django import forms
from django.forms import modelformset_factory
from .models import UserJob, Profile


class UserJobForm(forms.ModelForm):
    class Meta:
        model = UserJob
        fields = ("position", "location", "employer")

UserJobFormSet = modelformset_factory(UserJob, form=UserJobForm)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("location", "picture",)
