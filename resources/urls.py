from django.urls import path

from . import views

urlpatterns = [
    path("resource_list", views.show_resources, name="resource_list"),
]