from django import forms
from .models import Invoice

# To take date in calendar
class DateInput(forms.DateInput):
    input_type = "date"


class InvoiceForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.name = ''  # This should remove the label

    class Meta:
        model = Invoice
        fields = '__all__'          # what you want to output in the html file
        labels = {
            'identifier' : ''     # To remove field's name
        }

        widgets = {'due_date': DateInput(),
                   'invoice_date': DateInput(),
                   'sender' : forms.Textarea(attrs={'rows' :10, 'cols':2}),
                   'to' : forms.Textarea(attrs={'size' : 1})

                   }
