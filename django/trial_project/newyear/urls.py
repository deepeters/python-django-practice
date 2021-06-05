from django.urls import path
from django.urls import __path__
from . import views

urlpatterns = [
    path("", views.index, name="index")
]