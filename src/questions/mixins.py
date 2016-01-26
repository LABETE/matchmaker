from django.contrib import messages
from django.shortcuts import redirect

from .models import Question, UserAnswer, Answer
from .signals import match


class PostQuestionMixin:
    def post(self, *args, **kwargs):
        question_id = self.request.POST.get("question_id")
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = Question.objects.get(pk=question_id)
            user_answer = UserAnswer.objects.filter(
                user=self.request.user,
                question=self.object).first()
            if not user_answer:
                user_answer = UserAnswer()
            # user
            answer_id = self.request.POST.get("answer_id")
            answer_obj = Answer.objects.get(id=answer_id)
            my_answer_importance = self.request.POST.get("importance_level")

            their_answer_id = self.request.POST.get("their_answer_id")
            if their_answer_id == "-1":
                their_answer_obj = None
                their_importance = "Not Important"
            else:
                their_answer_obj = Answer.objects.get(id=their_answer_id)
                their_importance = self.request.POST.get("their_importance_level")
            user_answer.user = self.request.user
            user_answer.question_id = question_id
            user_answer.my_answer = answer_obj
            user_answer.my_answer_importance = my_answer_importance
            user_answer.their_answer = their_answer_obj
            user_answer.their_importance = their_importance
            user_answer.save()
            messages.success(self.request, 'Your information was saved successfuly.', extra_tags="success")
            match.send(self.request.user)
            question = Question.objects.all().order_by("?").first()
            return redirect("questions:detail", pk=question.pk)
        else:
            self.object = Question.objects.get(pk=question_id)
            messages.error(self.request, 'An error occured, try again.', extra_tags="error")
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
