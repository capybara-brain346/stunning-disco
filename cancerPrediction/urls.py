from django.urls import path
from . import views

urlpatterns = [
    path("form", views.predictForm, name="getinputforprediction"),
    path("getprediction", views.getInput, name="getprediction"),
]
