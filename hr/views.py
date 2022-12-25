from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Employee, Status
from .forms import ProfileForm


@login_required
def show_newhire(request):
    employees = Employee.objects.all().filter(is_new=True).order_by('-status')
    statuses = Status.objects.values_list('name', flat=True)
    return render(request, "hr/newhire_list.html", {
        'employees' : employees,
        'statuses' : statuses
    })


@login_required
def edit_profile(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=employee)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('newhire_list'))

    else:
        profile_form = ProfileForm(instance=employee)
        return render(request, "hr/edit_profile.html", {
            "profile_form": profile_form,
            "employee": employee
        })