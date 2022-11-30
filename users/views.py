from django.shortcuts import render
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User
from .forms import UserForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.add_message(request, messages.ERROR, 'Invalid credentials.')
            return render(request, "users/login.html")
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out.')
    return render(request, "users/login.html")


def register(request):
    register_form = UserForm(request.POST)

    if request.method == "POST":

        if register_form.is_valid():
            username        = register_form.cleaned_data['username']
            email           = register_form.cleaned_data['email']
            password        = make_password(register_form.cleaned_data['password1'])
            role            = register_form.cleaned_data['role']

            user = User.objects.create(
                username = username,
                email = email,
                password = password,
                role = role
            )

            messages.add_message(request, messages.SUCCESS, 'Registered successfully. You can now login.')
            login(request, user)

            return HttpResponseRedirect(reverse("index"))
        # if form is invalid
        else:
            messages.add_message(request, messages.ERROR, 'Form is not valid.')

    return render(request, "users/register.html", {'register_form': register_form})
