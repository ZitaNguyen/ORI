from django.shortcuts import render
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Login
from hr.models import Employee


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        employee = Employee.objects.get(name=request.user)
        print(employee.role)
        if employee.role == 'employee':
            return render(request, "employee/resource_list.html", {"employee":employee}) # to modify
        else:
            return HttpResponseRedirect(reverse("newhire_list"))


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
            return render(request, "authentication/login.html")

    else:
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out.')
    return render(request, "authentication/login.html")


def register(request):
    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.add_message(request, messages.WARNING, 'Passwords must match.')
            return render(request, "authentication/register.html")

        # Attempt to create new user
        try:
            user = Login.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.add_message(request, messages.WARNING, 'Username already taken.')
            return render(request, "authentication/register.html")

        # Update user's permission to access database
        role = request.POST["role"]
        if (role == 'admin'):
            user.is_superuser = True
            user.is_staff = True
        elif (role == 'hr'):
            user.is_staff = True
        user.save()

        # Link user login account with employee table
        employee = Employee.objects.create(name=user, role=role)
        employee.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "authentication/register.html")
