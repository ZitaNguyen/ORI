from django.shortcuts import render


def show_resources(request):
    return render(request, "resources/resource_list.html")
