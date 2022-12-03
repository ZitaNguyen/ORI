from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Employee


@login_required
def show_newhire():
    return True
