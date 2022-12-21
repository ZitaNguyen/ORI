from django.urls import path

from . import views

urlpatterns = [
    path("newhire_list", views.show_newhire, name="newhire_list"),
    path("edit_profile/<int:employee_id>", views.edit_profile, name="edit_profile")
]