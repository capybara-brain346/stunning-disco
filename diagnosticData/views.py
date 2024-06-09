from django.shortcuts import render
import pandas as pd
from cancerPrediction.models import cancerPreScreenData
from ctscanClassifier.models import cancerClassification


def dashboard(request):
    cancerPreScreen_df = pd.DataFrame(cancerPreScreenData.objects.all().values())
    cancerClassification_df = pd.DataFrame(cancerClassification.objects.all().values())
    return render(
        request,
        "data.html",
        {
            "data_record_cp": cancerPreScreen_df.drop("id", axis=1).to_html(),
            "data_record_ct": cancerClassification_df.drop("id", axis=1).to_html,
        },
    )
