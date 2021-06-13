from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDERS = [
        ("1", "male"),
        ("2", "female")
    ]

    gender = models.CharField(choices=GENDERS, max_length=64, default="1")
    age = models.IntegerField(null=True, blank=True, default=18)

   

class Diagnosis(models.Model):

    SEVERITIES = [
        ("3", "Low"), 
        ("2", "Medium"), 
        ("1", "High")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diagnoses")
    condition = models.CharField(null=True, blank=True, max_length=64)
    severity = models.CharField(choices=SEVERITIES, default="3", max_length=64)
    summary = models.TextField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=64)
    time = models.DateTimeField(null=True, blank=True)


