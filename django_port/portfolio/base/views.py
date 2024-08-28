from django.shortcuts import render
from .forms import *
from .models import Invoice

# PDF
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
# PDF

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    return HttpResponse(result.getvalue(), content_type='application/pdf')



def home(request) :

    return render(request, 'base/home.html')







def invoice_pdf(request) :

    form = InvoiceForm()
    if request.method == 'POST' :
        print(request.POST)
        form = InvoiceForm(request.POST)
        if form.is_valid() :
            print(form.cleaned_data)  # Access form data
            invoice = form.save()
            print("invoice saved")

            context = {'invoice': invoice}
            print(context['invoice'])
            # response = render_to_pdf('base/invoice_pdf.html', context)
            # return response
        else:
            print(form.errors)



    context = {'form' : form}
    return render(request, 'base/invoice_pdf.html', context)
