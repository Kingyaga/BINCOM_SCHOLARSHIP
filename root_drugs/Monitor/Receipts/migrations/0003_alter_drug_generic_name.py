# Generated by Django 4.2.6 on 2023-11-29 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0002_remove_receiptitem_drug_remove_receiptitem_receipt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='generic_name',
            field=models.CharField(max_length=200),
        ),
    ]
