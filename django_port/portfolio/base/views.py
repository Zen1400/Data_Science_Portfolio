from django.shortcuts import render
from .forms import *
from .models import Invoice

# Create your views here.


def home(request) :

    return render(request, 'base/home.html')



def invoice_pdf(request) :

    form = InvoiceForm()
    if request.method == 'POST' :

        form = InvoiceForm(request.POST)
        if form.is_valid() :
            form.save()



    context = {'form' : form}
    return render(request, 'base/invoice_pdf.html', context)
