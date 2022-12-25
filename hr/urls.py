from django.urls import path

from . import views

urlpatterns = [
    path("newhire_list", views.show_newhire, name="newhire_list"),
    path("view_profile/<int:employee_id>", views.view_profile, name="view_profile"),
    path("edit_profile/<int:employee_id>", views.edit_profile, name="edit_profile"),
    path("edit_status/<int:employee_id>", views.edit_status, name="edit_status"),
]