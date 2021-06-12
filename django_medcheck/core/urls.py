from django.urls import path, include

from core import views

urlpatterns = [
    path('get-location/', views.getLocation),
    path('create-diagnosis/', views.createDiagnosis),
    path('web-scrape/', views.webScrape),
    path('get-data/', views.getUserData),
    path('diagnoses/', views.DiagnosesList.as_view()),
]