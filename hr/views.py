import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, Http404
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt


from .models import Employee, Status, Task
from .forms import ProfileForm


@login_required
def show_newhire(request):
    # Get employee with status 'upcoming' or 'current'
    employees = Employee.objects.all().filter(Q(status=2) | Q(status=3)).order_by('start_date')
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

        # Get templates
        templates = profile_form.cleaned_data['template']
        # Get tasks from templates
        tasks = []
        for template in templates:
            tasks.extend(Task.objects.filter(template=template))
        # Add tasks for employee
        for task in tasks:
            employee.task.add(task)

        messages.add_message(request, messages.SUCCESS, 'Profile was updated.')
        return HttpResponseRedirect(reverse('view_profile', args=(employee_id,)))


@csrf_exempt
@login_required
def edit_status(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        employee.status = Status.objects.get(name=data["status"])
        employee.save()
        return HttpResponse(status=204)


@login_required
def view_profile(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Http404("employee not found")

    templates = employee.template.all()
    if not templates:
        tasks = None
    else:
        tasks = employee.task.all()

    profile_form = ProfileForm(instance=employee)
    return render(request, "hr/view_profile.html", {
        "profile_form": profile_form,
        "employee": employee,
        "templates": templates,
        "tasks": tasks
    })


@csrf_exempt
@login_required
def check_done(request, employee_id, task_id):
    if request.method == "PUT":
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)

        employee.task.remove(task_id)
        employee.save()

        return HttpResponse(status=204)