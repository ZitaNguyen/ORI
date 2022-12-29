from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Resource
from hr.models import Employee
from .forms import ResourceForm


@login_required
def show_resources(request):
    categories = Resource.objects.values_list('category', flat=True).distinct()
    return render(request, "resources/resource_list.html", {"categories": categories})



@login_required
def add_resource(request):
    if request.method == "POST":
        resource_form = ResourceForm(request.POST)
        if resource_form.is_valid():
            resource_form.save()
            return redirect('resource_list')

    else:
        resource_form = ResourceForm()
        return render(request, "resources/add_resource.html", {"resource_form":resource_form})


@login_required
def category_items(request, category):
    category_items = Resource.objects.filter(category=category)
    return render(request, "resources/category_items.html", {
        "items":category_items,
        "category":category
    })


@login_required
def show_contact(request):
    user = Employee.objects.get(name=request.user)
    teams = Employee.objects.filter(department=user.department)
    return render(request, "resources/contact_list.html", {"teams":teams, "username":user.name})


@login_required
def show_video(request):
    employee = Employee.objects.get(name=request.user)
    resources = Resource.objects.filter(category='training', sub_category=employee.department)
    print(resources)
    return render(request, "resources/training_video.html", {
        "resources": resources,
        "department": employee.department.name
    })