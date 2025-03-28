from django.urls import path  # type: ignore
from OTS.views import *

app_name = 'OTS'

urlpatterns = [
    path('', welcome, name='welcome'),  # Root path
    path('new-candidate/', candidateRegistrationForm, name='registrationForm'),
    path('store-candidate/', candidateRegistration, name='storeCandidate'),
    path('login/', loginView, name='login'),
    path('home/', candidateHome, name='home'),
    path('test-paper/', testPaper, name='testPaper'),
    path('calculate-result/', calculateTestResult, name='calculateTest'),
    path('test-history/', testResultHistory, name='testHistory'),
    path('result/', showTestResult, name='result'),
    path('logout/', logoutView, name='logout'),  # type: ignore
]
