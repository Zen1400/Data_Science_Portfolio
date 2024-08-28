from django.db import models

# Create your models here.

class Invoice(models.Model):

    English = """
            ZEIN MOUALLA
            IBAN - FR47 2004 1010 1114 3315 8P03 275
            BIC/SWIFT - PSSTFRPPNTE
            VAT Rate - 0.0%
            No VAT has been added to this invoice in accordance
            with EU law
            VAT exempt - EU Directive 2006/112/EC, Article 132, 1
            CRKBO accredited
            Tax Number (SIREN) : 920295805
             """

    French = """
            ZEIN MOUALLA
            4 Rue de l'étoile du Berger
            Bouguenais - Nantes
            zeinmou72@gmail.com
            +33652886958
            SIREN : 920295805
            IBAN - FR76 4061 8804 1000 0408 9387 149
            BIC/SWIFT - BOUSFRPPXXX
            VAT Rate - 0.0%
            TVA non applicable, article 293 B du Code Général des
            Impôts
            VAT exempt - EU Directive 2006/112/EC, Article 132, 1

            """

    sender_choices = (
        ("en", English),
        ("fr", French),
    )



    identifier = models.CharField(primary_key=True, max_length=50)
    sender = models.CharField(max_length=255, default=English)
    to = models.CharField(max_length=250)
    invoice_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default = 0)

    def __str__(self):
        return self.identifier
