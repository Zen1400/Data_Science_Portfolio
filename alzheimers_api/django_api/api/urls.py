from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('patient_input/', views.PatientInputAPIView.as_view(), name='patient_input_api'),
]
