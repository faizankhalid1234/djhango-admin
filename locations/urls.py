from django.urls import path

from . import views

urlpatterns = [
    path("", views.location_dropdown, name="location_dropdown"),
]

