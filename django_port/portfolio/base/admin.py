from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm
# Register your models here.


# Create a Class to show Invoices in a table

class InvoiceAdming(admin.ModelAdmin):
    list_display = ["identifier", "invoice_date", "total_amount"]
    form = InvoiceForm
    list_filter = ["identifier"]
    search_fields = ["identifier"]




admin.site.register(Invoice, InvoiceAdming)
