from django import forms
from .models import *
from dal import autocomplete

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'address', 'email', 'phone_number']

    def clean_supplier_name(self):
        supplier_name = self.cleaned_data['supplier_name']
        regex_validator = RegexValidator(
            regex=r'[a-zA-Z]+',
            message='Supplier name must contain words.',
            code='invalid_supplier_name'
        )
        regex_validator(supplier_name)  # Validate using the RegexValidator
        return supplier_name

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['drug_name', 'generic_name']

class ReceiptForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label="Select Supplier")
    supply_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = SupplierSupply
        fields = ['supplier', 'supply_date']

class ProductReceiptForm(forms.ModelForm):
    class Meta:
        model = SupplierSupply
        fields = ['content_type', 'object_id', 'content_object', 'quantity_added', 'cost_price', 'former_quantity']
        widgets = {
            'content_type': forms.HiddenInput(),  # Hidden input for content type
            'object_id': forms.HiddenInput(),  # Hidden input for object ID
            'content_object': autocomplete.ModelSelect2(
                url='Receipts:product-autocomplete',
                attrs={'data-minimum-input-length': 2}
            ),
            'quantity_added': forms.NumberInput(),
            'cost_price': forms.NumberInput(),
            'former_quantity': forms.NumberInput(),
        }

ProductReceiptFormSet = forms.modelformset_factory(
    SupplierSupply,
    form=ProductReceiptForm,
    extra=1,
)