from django.urls import path
from . import views

urlpatterns = [
    path("form", views.predictForm, name="getinputforprediction"),
    path("getprediction", views.getFormInput, name="getprediction"),
    path("getbatchprediction", views.getCSVInput, name="getbatchprediction"),
]
