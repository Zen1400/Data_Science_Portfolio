# Generated by Django 5.1 on 2024-08-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='item_description',
            field=models.CharField(default='New item', max_length=255),
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='invoice',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='InvoiceItem',
        ),
    ]
