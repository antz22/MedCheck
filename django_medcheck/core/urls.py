from django.urls import path, include

from core import views

urlpatterns = [
    path('get-data/', views.getUserData),
    path('create-diagnosis/', views.createDiagnosis),
    path('web-scrape/', views.webScrape),
    path('diagnoses/', views.DiagnosesList.as_view()),
]