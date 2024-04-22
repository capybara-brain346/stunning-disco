from django.shortcuts import render
import pandas as pd
from cancerPrediction.models import cancerPreScreenData
from ctscanClassifier.models import cancerClassification


def dashboard(request):
    cancerPreScreen_df = pd.DataFrame(cancerPreScreenData.objects.all().values())
    print(cancerPreScreen_df)
    return render(request, "data.html", {"data_record": cancerPreScreen_df.to_html()})
