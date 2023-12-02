from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from .forms import *

def index(request):
    return render(request, 'Receipts/index.html')

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'Receipts/supplier_list.html', {'suppliers': suppliers})

def supplier_details(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    supplier_supplies = SupplierSupply.objects.filter(supplier_id=supplier_id).order_by('-supply_date').values_list('supply_date', flat=True).distinct()
    return render(request, 'Receipts/supplier_details.html', {'supplier': supplier, 'supplier_supplies': supplier_supplies, 'supplier_id': supplier_id})

def search_drug_history(request):
    if 'query' in request.GET:
        query = request.GET['query']
        # Perform case-insensitive search for drug name or generic name
        drugs = Drug.objects.filter(models.Q(drug_name__icontains=query) | models.Q(generic_name__icontains=query))
        return render(request, 'Receipts/drug_search_results.html', {'drugs': drugs, 'query': query})
    return render(request, 'Receipts/search_drug_history.html')

def drug_details(request, drug_id):
    drug = get_object_or_404(Drug, pk=drug_id)
    supplies = SupplierSupply.objects.filter(drug=drug)
    return render(request, 'Receipts/drug_details.html', {'drug': drug, 'supplies': supplies})

def Receipt_details(request, supply_id):
    supply = get_object_or_404(SupplierSupply, pk=supply_id)
    return render(request, 'Receipts/Receipt_details.html', {'supply': supply})

def receipt(request, supplier_id):
    if request.method == 'GET':
        supply_date = request.GET.get('supply_date')
        if not supply_date:
            messages.error(request, 'Supply date is missing.')
            return HttpResponseBadRequest('Supply date is missing.')
        supplier = get_object_or_404(Supplier, pk=supplier_id)
        supplies = SupplierSupply.objects.filter(supplier=supplier, supply_date=supply_date)
        return render(request, 'Receipts/receipt.html', {'supplier': supplier, 'supplies': supplies, 'supply_date': supply_date})
    else:
        return HttpResponseBadRequest('Invalid request method.')

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier_name = form.cleaned_data['supplier_name']
            # Check if a supplier with the same name already exists
            existing_supplier = Supplier.objects.filter(supplier_name__iexact=supplier_name).first()
            if existing_supplier:
                # If the supplier already exists, redirect to a view or page showing the existing supplier details
                return redirect('supplier-details', supplier_id=existing_supplier.id)
            else:
                # If the supplier does not exist, save the new supplier
                form.save()
                return redirect('supplier-list')  # Redirect to a view showing the list of suppliers
    else:
        form = SupplierForm()
    return render(request, 'Receipts/add-supplier.html', {'form': form})

def add_drug(request):
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            drug_name = form.cleaned_data['drug_name']
            # Check if a drug with the same name already exists
            existing_drug = Drug.objects.filter(drug_name__iexact=drug_name).first()
            if existing_drug:
                # If the drug already exists, redirect to a view or page showing the existing drug details
                return redirect('drug-details', drug_id=existing_drug.id)
            else:
                # If the drug does not exist, save the new drug
                form.save()
                return redirect('drug-details', drug_id=existing_drug.id)  # Redirect to a view showing the drug details
    else:
        form = DrugForm()
    return render(request, 'Receipts/add-drug.html', {'form': form})

def add_receipt(request):
    if request.method == 'POST':
        receipt_form = ReceiptForm(request.POST)
        drug_receipt_formset = DrugReceiptFormSet(request.POST, queryset=SupplierSupply.objects.none())

        if receipt_form.is_valid() and drug_receipt_formset.is_valid():
            cleaned_data = receipt_form.cleaned_data
            supplier = cleaned_data.get('supplier')
            supply_date = cleaned_data.get('supply_date')
            # Link each drug receipt to the main receipt instance
            drug_receipt_instances = drug_receipt_formset.save(commit=False)
            for instance in drug_receipt_instances:
                instance.supplier = supplier
                instance.supply_date = supply_date
                instance.save()

            return redirect('index')  # Redirect to a view showing a list of receipts
    else:
        receipt_form = ReceiptForm()
        drug_receipt_formset = DrugReceiptFormSet(queryset=SupplierSupply.objects.none())

    return render(request, 'Receipts/add-receipt.html', {
        'receipt_form': receipt_form,
        'drug_receipt_formset': drug_receipt_formset
    })

class DrugAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Drug.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs