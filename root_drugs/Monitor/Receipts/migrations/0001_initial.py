# Generated by Django 4.2.6 on 2023-11-29 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_date', models.DateField()),
                ('quantity_supplied', models.IntegerField(default=0)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('initial_quantity', models.IntegerField(default=0)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.drug')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_purchased', models.IntegerField(default=0)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_quantity', models.IntegerField(default=0)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.drug')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Receipts.receipt')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receipts.supplier'),
        ),
    ]
