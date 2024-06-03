from django.shortcuts import render
from django.conf import settings
from ctscanClassifier.models import cancerClassification
import cv2
import numpy as np
from tensorflow.keras.models import load_model


def db_commit(patient_info, cancer_type):
    member = cancerClassification(
        name=patient_info[1],
        email=patient_info[2],
        phone=patient_info[3],
        classification=cancer_type,
    )
    member.save()
    print(cancerClassification.objects.all().values())
    return None


def preprocess_image(input_image):
    nparr = np.frombuffer(input_image.read(), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_array = np.array(image)
    img_array = cv2.resize(img_array, (256, 256))
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def get_prediction(input_img):
    model = load_model(r"ctscanClassifier\artifacts\Lung_Model.h5")
    prediction_array = model.predict(input_img)
    class_label = np.argmax(prediction_array)
    class_labels_to_categories = {0: "Benign", 1: "Malignant", 2: "Normal"}
    predicted_category = class_labels_to_categories[class_label]
    return predicted_category


def classifyForm(request):
    return render(request, "classification_form.html")


def getImageInput(request):
    if request.method == "POST":
        form = request.POST
        form_data = [val for key, val in form.items()]

        image = request.FILES["lung_scan"]

        processed_image = preprocess_image(image)
        prediction = get_prediction(processed_image)

        db_commit(patient_info=form_data, cancer_type=prediction)

        return render(
            request,
            "classification_form.html",
            {"classification": prediction},
        )

    else:
        return render(request, "classification_form.html")
