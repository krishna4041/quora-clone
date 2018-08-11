from django.forms import ModelForm
from django import forms
from quoraapp.models import *

class Answerform(forms.ModelForm):
    class Meta:
        model=Answer
        exclude = ['id','answer_by','for_question_id','upvote','for_question','for_flag']
        Answer_text = forms.TextInput()