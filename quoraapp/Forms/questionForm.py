from django.forms import ModelForm
from django import forms
from quoraapp.models import *

class Questionform(forms.ModelForm):
    class Meta:
        model=Question
        exclude = ['id','question_by','user_id','user']
        Question_text = forms.CharField(
            max_length=75,
            widget=forms.TextInput(),
            required=True,
        )