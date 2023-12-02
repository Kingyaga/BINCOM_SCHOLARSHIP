from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Drug)
admin.site.register(SupplierSupply)