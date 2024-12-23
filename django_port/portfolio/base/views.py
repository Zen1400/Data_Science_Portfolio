from django.shortcuts import render
from .models import Invoice
import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from datetime import date






def home(request) :

    return render(request, 'base/home.html')



def invoice_management(request) :

    return render(request, 'base/test.html')




def generate_invoice_pdf(request):
    if request.method == 'POST':
        # Extract form data
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        due_date = request.POST.get('due_date')
        company_info = request.POST.get('company_info')
        # company_address = request.POST.get('company_address')
        # company_email = request.POST.get('company_email')
        # company_phone = request.POST.get('company_phone')
        client_info = request.POST.get('client_info')
        # client_address = request.POST.get('client_address')
        # client_email = request.POST.get('client_email')
        # client_phone = request.POST.get('client_phone')
        descriptions = request.POST.getlist('description[]')
        unit_prices = request.POST.getlist('unit_price[]')
        quantities = request.POST.getlist('quantity[]')
        total_amount = request.POST.get('total_amount')
        notes = request.POST.get("notes")
        # bank_name = request.POST.get('bank_name')
        # bank_account = request.POST.get('bank_account')
        # swift_bic = request.POST.get('swift_bic')

        # Prepare items
        items = []
        for desc, price, qty in zip(descriptions, unit_prices, quantities):
            total = float(price) * int(qty)
            items.append({
                'description': desc,
                'unit_price': f"{price}",
                'quantity': qty,
                'total': f"{total:.2f}"
            })

        context = {
            'invoice_number': invoice_number,
            'invoice_date': invoice_date,
            'due_date' : due_date,
            'company_info': company_info,
            # 'company_address': company_address,
            # 'company_email': company_email,
            # 'company_phone': company_phone,
            'client_info': client_info,
            # 'client_address': client_address,
            # 'client_email': client_email,
            # 'client_phone': client_phone,
            'items': items,
            'total_amount': total_amount,
            # 'bank_name': bank_name,
            # 'bank_account': bank_account,
            # 'swift_bic': swift_bic,
        }

        if invoice_number :
            # save the invoice to the database
            invoice = Invoice.objects.create(
                invoice_number = invoice_number,
                company_info = company_info,
                client_info = client_info,
                due_date = due_date,
                invoice_date = invoice_date,
                total_amount = total_amount

            )

        # Render HTML
        html = render_to_string('base/simple_invoice.html', context)

        # Configure pdfkit options
        options = {
            'page-size': 'A4',
            'encoding': "UTF-8",
            'enable-local-file-access': None  # Important for accessing local CSS files
        }

        # Path to wkhtmltopdf executable
        config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)

        # Generate PDF
        pdf = pdfkit.from_string(html, False, configuration=config, options=options)

        # Create HTTP response
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice_number}.pdf"'

        return response

    # return HttpResponse('Invalid request', status=400)
    return render(request, 'base/simple_invoice.html')
