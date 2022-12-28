from django.shortcuts import render
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Login
from hr.models import Employee, Role, Status
from .forms import RegisterForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        employee = Employee.objects.get(name=request.user)
        user_role = Role.objects.get(name=employee.role)
        if user_role.name == 'employee':
            return HttpResponseRedirect(reverse("resource_list"))
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
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username        = register_form.cleaned_data['username']
            email           = register_form.cleaned_data['email']
            password        = register_form.cleaned_data['password']
            confirmation    = register_form.cleaned_data['confirmation']
            role            = register_form.cleaned_data['role']

            # Ensure password matches confirmation
            if password != confirmation:
                messages.add_message(request, messages.WARNING, 'Passwords must match.')
                return render(request, "authentication/register.html", {"register_form": register_form})

            # Attempt to create new user
            try:
                user = Login.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                messages.add_message(request, messages.WARNING, 'Username already taken.')
                return render(request, "authentication/register.html", {"register_form": register_form})

            # Update user's permission to access database
            if (role == 'admin'):
                user.is_superuser = True
                user.is_staff = True
            elif (role == 'hr'):
                user.is_staff = True
            user.save()

            # Link user login account with employee table
            if (role == 'employee'):
                # Get role id
                role_id = Role.objects.get(name='employee')
                # Get status id
                status_id = Status.objects.get(name='upcoming')
                # Create employee
                employee = Employee.objects.create(name=user, role=role_id, is_new=True, status=status_id)
            else:
                # Get role id
                role_id = Role.objects.get(name=role)
                # Get status id
                status_id = Status.objects.get(name='done')
                # Create employee
                employee = Employee.objects.create(name=user, role=role_id, status=status_id)
            employee.save()

            login(request, user)
            return HttpResponseRedirect(reverse("index"))

    else:
        register_form = RegisterForm()
        return render(request, "authentication/register.html", {"register_form": register_form})
