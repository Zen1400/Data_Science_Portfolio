from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
     path('invoice/', views.generate_invoice_pdf, name='invoice_pdf'),
]
