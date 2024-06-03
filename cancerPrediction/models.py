from django.db import models

gender_choices = [("male", "male"), ("female", "female")]


class cancerPreScreenData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=gender_choices, max_length=10)
    phone = models.IntegerField()
    cancer_risk = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.cancer_risk}"
