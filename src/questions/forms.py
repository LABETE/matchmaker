from django import forms

from .models import LEVELS, Answer


class QuestionForm(forms.Form):
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()
    importance_level = forms.ChoiceField(choices=LEVELS)
    their_answer_id = forms.IntegerField()
    their_importance_level = forms.ChoiceField(choices=LEVELS)

    def clean_answer_id(self):
        answer_id = self.cleaned_data.get("answer_id")
        try:
            obj = Answer.objects.get(id=answer_id)
        except:
            raise forms.ValidationError("Selected option does not exist.")
        return answer_id

    def clean_ther_answer_id(self):
        their_answer_id = self.cleaned_data.get("their_answer_id")
        try:
            obj = Answer.objects.get(id=their_answer_id)
        except:
            if their_answer_id == -1:
                return their_answer_id
            raise forms.ValidationError("Selected option does not exist.")
        return their_answer_id
