from django.urls import path
from . import views

urlpatterns = [
    path("form", views.classifyForm, name="getinputforclassification"),
    path("getclassification", views.getImageInput, name="getclassification"),
]
