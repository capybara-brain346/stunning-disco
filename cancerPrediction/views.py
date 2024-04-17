from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, "index.html")


def getPrediction(request):
    return render(request, "predict.html")
