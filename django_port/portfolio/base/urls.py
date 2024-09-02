from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
     path('generate_invoice/', views.generate_invoice_pdf, name='invoice_pdf'),
     path('invoice/', views.invoice_management, name = 'invoice_management'),
]
