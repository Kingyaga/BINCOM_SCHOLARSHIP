# Generated by Django 4.2.6 on 2023-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receipts', '0007_remove_supplier_contact_info_supplier_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
