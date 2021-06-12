from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDERS = [
        ("1", "male"),
        ("2", "female")
    ]

    gender = models.CharField(choices=GENDERS)

   

class Diagnosis(models.Model):

    SEVERITIES = [
        ("3", "Low"), 
        ("2", "Medium"), 
        ("1", "High")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diagnoses")
    condition = models.CharField(null=True, blank=True)
    severity = models.CharField(choices=SEVERITIES, default="3")
    summary = models.TextField(null=True, blank=True)
    location = models.CharField(null=True, blank=True)


