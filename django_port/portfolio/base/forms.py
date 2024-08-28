from django import forms
from .models import Invoice

# To take date in calendar
class DateInput(forms.DateInput):
    input_type = "date"


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = '__all__'          # what you want to output in the html file
        labels = {
            'identifier' : '',
            'invoice_date' : '',
            'due_date' : '',
            'sender' : '',
            'total_amount' : '',
            'to' : '',
            # To remove field's name
        }

        widgets = {'due_date': DateInput(),
                   'invoice_date': DateInput(),
                #    'sender' : forms.Textarea(attrs={'rows' :10}),
                   'to' : forms.Textarea(attrs={'size' : 1}),
                   'total_amount': forms.NumberInput(attrs={'readonly': 'readonly'}),

                   }
