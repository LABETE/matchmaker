from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import ModelFormMixin



from likes.models import Like
from matches.models import Match
from profiles.models import UserJob
from questions.mixins import PostQuestionMixin
from questions.models import UserAnswer, Question, LEVELS
from questions.forms import QuestionForm
from .forms import ContactForm, SignUpForm
from .models import SignUp


class homeTemplateView(PostQuestionMixin, ModelFormMixin, TemplateView):
    template_name = "home.html"
    form_class = QuestionForm

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.object = Question.objects.get_unanswered_questions(self.request.user).order_by("?").first()
            positions = []
            locations = []
            employers = []
            context = super(homeTemplateView, self).get_context_data(*args, **kwargs)
            matches, users = Match.objects.get_match_all(self.request.user)[:6]
            jobs = UserJob.objects.filter(user__in=users).order_by("?")[:6]
            user_like = get_object_or_404(Like, user=self.request.user)
            context["answers"] = UserAnswer.objects.filter(
                user=self.request.user,
                question=self.object).first()
            if jobs:
                for job in jobs:
                    if job.position not in positions:
                        positions.append(job.position)
                    if job.location not in locations:
                        locations.append(job.location)
                    if job.employer not in employers:
                        employers.append(job.employer)
                context["positions"] = positions
                context["locations"] = locations
                context["employers"] = employers
            context["liked_users"] = user_like.liked_users.all()
            context["matches_list"] = matches
            context["question_object"] = self.object
            context["levels"] = LEVELS
            context["form"] = self.form_class
        return context


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youotheremail@email.com']
        contact_message = "%s: %s via %s" % (
            form_full_name,
            form_message,
            form_email)
        some_html_message = """
		<h1>hello</h1>
		"""
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=True)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)
