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
        fields = ['name', 'generic_name']

class ProvisionForm(forms.ModelForm):
    class Meta:
        model = Provision
        fields = ['name', 'category']

class ReceiptForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label="Select Supplier")
    supply_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Receipt
        fields = ['supplier', 'supply_date']

class ReceiptItemForm(forms.ModelForm):
    class Meta:
        model = ReceiptItem
        fields = ['item', 'quantity_added', 'cost_price', 'former_quantity']
        widgets = {
            'item': autocomplete.Select2(
                url='Receipts:autocomplete',
                attrs={'data-minimum-input-length': 2}
            )}

ReceiptItemFormSet = forms.modelformset_factory(
    ReceiptItem,
    form=ReceiptItemForm,
    extra=1,
)