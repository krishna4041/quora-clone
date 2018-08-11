from django.views import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from quoraapp.Forms.auth import *


class SignupView(View):
    def get(self, request):
        form = Signupform
        return render(
            request,
            template_name='signup.html',
            context={'form': Signupform}
        )

    def post(self, request):
        form = Signupform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                id=user.id
                login(request, user)
                return redirect('/login/')
            else:
                return render(
                    request,
                    template_name='signup.html',
                    context={
                        'form': form
                    }
                )


class Login_user(View):
    def get(self, request):
        loginform = Loginform
        return render(
            request,
            template_name='login.html',
            context={'form': loginform}
        )

    def post(self, request):
        form = Loginform(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user is not None:
                login(request, user)
                return redirect('/feed/')
            else:
                return render(
                    request,
                    'login.html',
                    {
                        'form': form
                    }
                )

def Logout_user(request):
    logout(request)
    return redirect('/login/')
