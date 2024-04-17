from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),
    path("getprediction/", views.getPrediction),
]
