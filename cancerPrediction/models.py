from django.db import models


class cancerPreScreenData(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    cancerPrediction = models.CharField(max_length=10)

    def __str__(self) -> str:
        return "%s %s %s", self.name, self.email, self.cancerPrediction
