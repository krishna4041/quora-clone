from django.forms import ModelForm,Textarea
from django import forms
from django.contrib.auth.models import User
from quoraapp.models import *
from django.contrib.auth.forms import UserChangeForm


class Signupform(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=75,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last Name", max_length=75,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label="Email", max_length=75,
                             widget=forms.TextInput(attrs={'placeholder': "example@email.com"}))
    username = forms.CharField(label="User Name", max_length=75,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                            help_text = False)
    password = forms.CharField(widget=forms.PasswordInput)



class Loginform(forms.Form):
    username=forms.CharField(
        max_length=75,
        widget=forms.TextInput(attrs={'placeholder': 'username'}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
        required=True
    )

class EditUserProfileForm(ModelForm):
    class Meta:
        model = User
        fields=('first_name','last_name','username','email')
        help_texts = {
            'username': None,
            'email': None,
        }
        widgets = {
            "status": forms.Textarea(attrs={"class": "form-control"})
        }
