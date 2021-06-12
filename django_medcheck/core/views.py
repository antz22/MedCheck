import json

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import User, Diagnosis
from .serializers import DiagnosisSerializer


class DiagnosesList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        diagnoses = Diagnosis.objects.filter(user=request.user)
        serializer = DiagnosisSerializer(diagnoses, many=True)
        return Response(serializer.data)




@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def createDiagnosis(request):

    diagnosis_data = request.data

    condition = diagnosis_data['condition']
    severity = diagnosis_data['severity']
    summary = diagnosis_data['summary']
    location = diagnosis_data['location']

    diagnosis = Diagnosis.objects.create(user=request.user, condition=condition, severity=severity, summary=summary location=location)
    diagnosis.save()

    return Response(status=status.HTTP_201_CREATED)



# def webScrape(request):

