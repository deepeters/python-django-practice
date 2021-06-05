from django.urls import __path__
from django.urls.conf import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("dennis", views.dennis, name="dennis"),
    path("esther", views.esther, name="esther"),
]