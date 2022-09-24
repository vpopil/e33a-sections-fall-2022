from django.urls import path

from . import views

app_name = "budget"
urlpatterns = [
    path("", views.index, name="index"),
    path("add-category", views.add, name="add"),
]


# path("wiki/<str:title>", views.entry, name="entry"),