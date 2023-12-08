from django.db import models
from django.core.validators import RegexValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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
    drug_name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.drug_name
    
class Provision(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

class SupplierSupply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    supply_date = models.DateField()
    quantity_added = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    former_quantity = models.IntegerField(default=0)
    # Generic Foreign Key for referencing Provision or Drug
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')