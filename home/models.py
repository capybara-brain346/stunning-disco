from django.db import models


# Create your models here.
class userModel(models.Model):
    name = models.CharField(max_length=30)
    emailAddress = models.EmailField(max_length=30)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=12)

    def __str__(self) -> str:
        return f"{self.username}"
