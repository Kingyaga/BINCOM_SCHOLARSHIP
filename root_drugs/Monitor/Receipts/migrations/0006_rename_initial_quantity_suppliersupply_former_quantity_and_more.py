# Generated by Django 4.2.6 on 2023-11-30 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0005_alter_suppliersupply_cost_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliersupply',
            old_name='initial_quantity',
            new_name='former_quantity',
        ),
        migrations.RenameField(
            model_name='suppliersupply',
            old_name='quantity_supplied',
            new_name='quantity_added',
        ),
    ]
