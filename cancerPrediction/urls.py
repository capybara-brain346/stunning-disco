from django.urls import path
from . import views

urlpatterns = [
    path("form", views.predictform, name="cancerpredict"),
    path("getprediction", views.getInput, name="getinput"),
]
