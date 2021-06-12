import json

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import os


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



def webScrape(request):
    scrape_data = request.data 

    # fill in webscraping code

    driver = webdriver.Firefox(executable_path='geckodriver')
    driver.get("https://www.malacards.org/")

    diagnosis = scrape_data['condition']
    driver.find_element_by_xpath('//*[@id="search-box-input"]').send_keys(diagnosis)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/div[3]/input').click()

    driver.maximize_window()  # For maximizing window
    driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds

    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/table/tbody/tr[2]/td[5]/a')
    element.click()

    textInSummary = []
    textInSummary = driver.find_element_by_xpath('//*[@id="Summary"]/b[2]/a').text  # changed path

    numberOfTimesSeenPunctuation = 0
    i = 0
    finalSummary = []

    while True:
    	if i < 24:     #this is what we added
    		continue
        if numberOfTimesSeenPunctuation == 4:
            break
        if textInSummary[i] == '?' or textInSummary[i] == '.' or textInSummary[i] == '!':
            numberOfTimesSeenPunctuation += 1
        finalSummary.append(textInSummary[i])    # this is what we changed
        # oput.write(textInSummary[i])
        i += 1

    jsonStringSummary = json.dumps(finalSummary)  # this is what we added