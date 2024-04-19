from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import joblib


def labelTransform(array_item):
    hmap = {"female": 0, "male": 1, "no": 0, "yes": 1}
    if array_item in hmap.keys():
        return hmap.get(array_item)
    else:
        return array_item


def scalarTransform(array):
    scalar = joblib.load(r"cancerPrediction\artifacts\minmaxscaler.joblib")
    toTransform = array[1]
    array[1] = scalar.transform(np.array(toTransform).reshape(1, -1))[0][0]
    return array


def getPrediction(array):
    hmap = {0: "Low Risk", 1: "High Risk"}
    model = joblib.load(r"cancerPrediction\artifacts\modular_svm.joblib")
    prediction = model.predict(np.array(array).reshape(1, -1))
    return hmap.get(prediction[0])


def predictform(request):
    return render(request, "prediction_form.html")


def getInput(request):
    if request.method == "POST":
        form = request.POST
        form_data = [val for key, val in form.items()]
        input_array = scalarTransform(form_data[4:])
        input_array = list(map(labelTransform, input_array))
        print(input_array)
        prediction = getPrediction(input_array)

        return render(request, "prediction_form.html", {"prediction": prediction})
    else:
        return render(
            request, "prediction_form.html", {"form_submission": "No form received"}
        )
