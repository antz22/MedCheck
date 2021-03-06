import json
import time
import csv
import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from .models import User, Diagnosis
from .serializers import DiagnosisSerializer

import requests
import datetime

class DiagnosesList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        diagnoses = Diagnosis.objects.filter(user=request.user)
        serializer = DiagnosisSerializer(diagnoses, many=True)
        return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getUserData(request):

    user = request.user 

    diagnoses = len(Diagnosis.objects.filter(user=user))

    if diagnoses == 0:
        lastdate = "No diagnoses!"

    else: 
        lastdate = Diagnosis.objects.filter(user=user).latest('id').time

    critical = len(Diagnosis.objects.filter(user=request.user, severity="3"))
    gender = user.gender
    if gender == "1":
        gender = "male"
    else:
        gender = "female"
    age = user.age
    username = user.username

    return Response({'diagnoses': diagnoses, 'critical': critical, 'gender': gender, 'age': age, 'name': username, 'lastdate': lastdate})




@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def createDiagnosis(request):

    diagnosis_data = request.data

    condition = diagnosis_data['condition']

    SEVERITIES = {
        'Cold': '1',
        'Constipation': '1',
        'Coronary Heart Disease': '3',
        'Depression': '3',
        'Strain of the back muscles': '2',
        'Sperm cyst': '3',
        'Drug side effect': '1',
        'Smoking': '2',
        'Slip disc': '3',
        'Anxiety': '3',
        'Influenza': '2',
        'Shaking Palsy': '3',
        'Scarlet Fever': '3',
        'Reflux disease': '2',
        'Pregnancy': '3',
        'Hernia': '3',
        'Huntington\'s disease': '3',
        'Menopause': '2',
        'Malignant Prostate Cancer': '3',
        'Lyme Disease': '3',
        'Loose watery stools': '2',
        'Listeria Infection': '3',
    }

    try:

        severity = SEVERITIES[condition]
    
    except KeyError:
        severity = '1'

    summary = diagnosis_data['summary']
    location = diagnosis_data['location']

    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day

    date = datetime.datetime(year, month, day)

    time = date.strftime("%b %d, %Y")

    diagnosis = Diagnosis.objects.create(user=request.user, condition=condition, severity=severity, summary=summary, location=location, time=time)
    diagnosis.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
@csrf_exempt
def webScrape(request):

    scrape_data = request.data
    diagnosis = scrape_data['condition']

    # fill in webscraping code

    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get("https://www.malacards.org/")

    driver.find_element_by_xpath('//*[@id="search-box-input"]').send_keys(diagnosis)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/div[3]/input').click()

    driver.maximize_window()  # For maximizing window
    driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds

    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/table/tbody/tr[2]/td[5]/a')
    element.click()

    textInSummary = []
    textInSummary = driver.find_element_by_xpath('//*[@id="Summary"]').text  # changed path

    numberOfTimesSeenPunctuation = 0
    i = 0
    finalSummary = []

    print(textInSummary)

    deletedPrev = False

    while True:
        print(finalSummary)
        if deletedPrev == False:
            # check if its a number, between 0 and 9
            if ord(textInSummary[i]) >= 48 and ord(textInSummary[i]) <= 57 and textInSummary[i+1] == ' ':
                textInSummary = textInSummary[i+2:]
                deletedPrev = True
                i = 0
            else:
                i += 1

        else:
            if numberOfTimesSeenPunctuation == 4:
                break
            if textInSummary[i] == '?' or textInSummary[i] == '.' or textInSummary[i] == '!':
                numberOfTimesSeenPunctuation += 1
            
            finalSummary.append(textInSummary[i])    # this is what we changed
            i += 1
    
    finalSummary = ''.join(finalSummary)
    
    driver.quit()


    # should return json
    return Response({'summary': finalSummary}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getLocation(request):
    
    req_data = request.data
    severity = req_data['severity']
    
    URL = "https://discover.search.hereapi.com/v1/discover"
    latitude = 40.421249
    longitude = -74.702431
    api_key = 'JsnHjC1KLaPcvfi82Pn_IK9diu9AaGkVAyKVWKDb1p0'
    query = 'pharmacies'

    if (severity == 3):
        return "Stay at home"
    elif (severity == 1):
        query = 'hospitals'
    limit = 5

    PARAMS = {
            'apikey':api_key,
            'q':query,
            'limit': limit,
            'at':'{},{}'.format(latitude,longitude)
         }

    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    
    return Response(data)
