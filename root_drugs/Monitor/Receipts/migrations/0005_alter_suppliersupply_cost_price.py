# Generated by Django 4.2.6 on 2023-11-30 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0004_alter_supplier_supplier_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliersupply',
            name='cost_price',
            field=models.IntegerField(default=0),
        ),
    ]
