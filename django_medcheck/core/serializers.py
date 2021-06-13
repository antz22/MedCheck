from rest_framework import serializers

from .models import User, Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = (
            "id",
            "condition",
            "severity",
            "summary",
            "location",
            "time",
        )