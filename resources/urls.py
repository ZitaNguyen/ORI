from django.urls import path

from . import views

urlpatterns = [
    path("resource_list", views.show_resources, name="resource_list"),
    path("add_resource", views.add_resource, name="add_resource"),
]