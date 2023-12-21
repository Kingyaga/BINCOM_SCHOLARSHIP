from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(
    max_length=200,
    unique=True,
    validators=[RegexValidator(
        regex=r'[a-zA-Z]+',
        message='Supplier name must contain words.',
        code='invalid_supplier_name'
    )]
    )
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.supplier_name
    
class Drug(models.Model):
    name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.drug_name
    
    def get_model_name(self):
        return 'Drug'
    
class Provision(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name
    
    def get_model_name(self):
        return 'Provision'  
    
class Item(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    provision = models.ForeignKey(Provision, on_delete=models.CASCADE)

class Receipt(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supply_date = models.DateField()

class ReceiptItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_added = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    former_quantity = models.IntegerField(default=0)