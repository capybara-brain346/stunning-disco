from django.shortcuts import render
from django.http import HttpResponse
from cancerPrediction.models import cancerPreScreenData
import pandas as pd
import numpy as np
import joblib


def db_commit(patient_info, risk):
    member = cancerPreScreenData(
        name=patient_info[1],
        email=patient_info[2],
        phone=patient_info[3],
        age=patient_info[5],
        gender=patient_info[4],
        cancer_risk=risk,
    )
    member.save()
    print(cancerPreScreenData.objects.all().values())
    return None


def db_commit_csv(patient_data):

    field_len = len(patient_data)
    for model_object in range(field_len):
        data_to_be_committed = patient_data.iloc[model_object, :]
        member = cancerPreScreenData(
            name=data_to_be_committed[0],
            email=data_to_be_committed[1],
            phone=data_to_be_committed[2],
            gender=data_to_be_committed[3],
            age=data_to_be_committed[4],
            cancer_risk=data_to_be_committed[5],
        )
        member.save()

    print(cancerPreScreenData.objects.all().values())
    return None


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


def scalarTransformCSV(array):
    scalar = joblib.load(r"cancerPrediction\artifacts\minmaxscaler.joblib")
    arrayTransformed = scalar.transform(np.array(array).reshape(-1, 1))
    return arrayTransformed


def labelTransformCSV(data):
    hmap = {"female": 0, "male": 1, "no": 0, "yes": 1}
    tobeTransformed = [
        "Gender",
        "Smoking",
        "Yellow Fingers",
        "Anxiety",
        "Peer Pressure",
        "Chronic Disease",
        "Fatigue",
        "Allergies",
        "Wheezing",
        "Alcohol",
        "Coughing",
        "Shortness of breath",
        "Shwallowing difficulty",
        "Chest pain",
    ]

    for cols in tobeTransformed:
        data[cols] = data[cols].replace(hmap)

    return data


def getPredictionCSV(data):
    hmap = {0: "Low Risk", 1: "High Risk"}
    model = joblib.load(r"cancerPrediction\artifacts\modular_svm.joblib")
    prediction = model.predict(data)
    return [hmap.get(risk) for risk in prediction]


def predictForm(request):
    return render(request, "prediction_form.html")


def getFormInput(request):
    if request.method == "POST":
        form = request.POST
        form_data = [val for key, val in form.items()]
        input_array = scalarTransform(form_data[4:])
        input_array = list(map(labelTransform, input_array))
        prediction = getPrediction(input_array)

        db_commit(form_data, prediction)

        return render(
            request,
            "prediction_form.html",
            {"prediction": prediction, "prediction_csv": " "},
        )
    else:
        return render(
            request, "prediction_form.html", {"form_submission": "No form received"}
        )


def getCSVInput(request):
    if request.method == "POST":
        if "csvsubmission" in request.FILES:
            form = request.FILES["csvsubmission"]
            csv_df = pd.read_csv(form)
            final_data = csv_df.iloc[:, :5]
            csv_df["Age"] = scalarTransformCSV(csv_df["Age"])
            input_data = labelTransformCSV(csv_df)
            prediction_col = getPredictionCSV(input_data.iloc[:, 3:])
            final_data["Risk"] = prediction_col
            db_commit_csv(final_data)
            return render(
                request,
                "prediction_form.html",
                {
                    "prediction": " ",
                    "prediction_csv": final_data.to_html(
                        classes="table table-striped table-bordered"
                    ),
                    "data": cancerPreScreenData.objects.all().values(),
                },
            )
        else:
            return HttpResponse("No CSV file submitted", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)
