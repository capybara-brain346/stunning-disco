from django.db import models


# Create your models here.
class cancerClassification(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    classification = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.classification}"
