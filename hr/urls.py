from django.urls import path

from . import views

urlpatterns = [
    path("newhire_list", views.show_newhire, name="newhire_list"),
]