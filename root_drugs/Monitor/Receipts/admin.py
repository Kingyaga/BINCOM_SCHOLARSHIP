from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Drug)
admin.site.register(ReceiptItem)
admin.site.register(Item)
admin.site.register(Receipt)
admin.site.register(Provision)