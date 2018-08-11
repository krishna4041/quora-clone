from django.forms import ModelForm
from django import forms
from quoraapp.models import *

class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        exclude = ['id','comment_by','for_comment_id','for_comment']
        Comment_text = forms.TextInput()

