from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"),
    path("form/edit/<pk>", views.edit, name="edit"),
    path("form/delete/<pk>", views.delete, name="delete"),
]

