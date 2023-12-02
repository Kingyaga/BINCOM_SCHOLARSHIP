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

class DrugReceiptForm(forms.ModelForm):
    class Meta:
        model = SupplierSupply
        fields = ['drug', 'quantity_added', 'cost_price', 'former_quantity']
        widgets = {
            'drug': autocomplete.Select2(
                url='drug-autocomplete',
                attrs={'data-minimum-input-length': 2}
            )}

DrugReceiptFormSet = forms.modelformset_factory(
    SupplierSupply,
    form=DrugReceiptForm,
    extra=1,
)