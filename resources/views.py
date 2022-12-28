from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Resource
from .forms import ResourceForm


@login_required
def show_resources(request):
    resources = Resource.objects.all()
    return render(request, "resources/resource_list.html", {"resources":resources})



@login_required
def add_resource(request):
    resource_form = ResourceForm(request.POST)

    if request.method == "POST":
        if resource_form.is_valid():
            resource_form.save()
        return HttpResponseRedirect(reverse('resource_list'))

    return render(request, "resources/add_resource.html", {"resource_form":resource_form})
