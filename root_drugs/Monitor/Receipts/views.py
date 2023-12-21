from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from itertools import chain
from django.db.models import Q
from .util import check_model_in_models
from .forms import *

def index(request):
    return render(request, 'Receipts/index.html')

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'Receipts/supplier_list.html', {'suppliers': suppliers})

def supplier_details(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    supplier_supplies = Receipt.objects.filter(supplier=supplier_id).order_by('-supply_date').values_list('supply_date', flat=True).distinct()
    return render(request, 'Receipts/supplier_details.html', {'supplier': supplier, 'supplier_supplies': supplier_supplies, 'supplier_id': supplier_id})

def search_item_history(request):
    if 'query' in request.GET:
        query = request.GET['query']
        # Perform case-insensitive search for drug name, generic name, provision name, and category
        drugs = Drug.objects.filter(Q(name__icontains=query) | Q(generic_name__icontains=query))
        provisions = Provision.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
        
        # Merge the querysets of drugs and provisions into a single queryset
        results = list(chain(drugs, provisions))
        return render(request, 'Receipts/item_search_results.html', {'results': results, 'query': query})
    return render(request, 'Receipts/search_item_history.html')

def item_details(request, item_type, item_id):
    if check_model_in_models(item_type):
        item = get_object_or_404(f"{item_type}", pk=item_id)
    else:
        # Handle invalid item type
        return HttpResponseBadRequest("Invalid item type")
    # Define a Q object to conditionally filter by drug_id or provision_id
    filter_condition = Q()
    if item_type == "Drug":
        filter_condition |= Q(items__item__drug_id=item_id)
    else:
        filter_condition |= Q(items__item__provision_id=item_id)
    # Query to get receipt details based on item_type (drug or provision)
    receipts = Receipt.objects.filter(filter_condition)
    return render(request, 'Receipts/item_details.html', {'item': item, 'type': item_type, 'receipts': receipts})

def Receipt_details(request, type, item_id, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id)
    item = receipt.items.filter(pk=item_id).first()
    return render(request, 'Receipts/Receipt_details.html', {'receipt': receipt, 'item': item, 'type': type})

def receipt(request, supplier_id):
    if request.method == 'GET':
        supply_date = request.GET.get('supply_date')
        if not supply_date:
            messages.error(request, 'Supply date is missing.')
            return HttpResponseBadRequest('Supply date is missing.')
        supplier = get_object_or_404(Supplier, pk=supplier_id)
        supplies = Receipt.objects.filter(supplier=supplier_id, supply_date=supply_date)
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
            drug_name = form.cleaned_data['name']
            # Check if a drug with the same name already exists
            existing_drug = Drug.objects.filter(name__iexact=drug_name).first()
            if existing_drug:
                # If the drug already exists, redirect to a view or page showing the existing drug details
                return redirect('item-details', item_type="Drug", item_id=existing_drug.id)
            else:
                # If the drug does not exist, save the new drug
                form.save()
                return redirect('item-details', item_type="Drug", item_id=existing_drug.id)  # Redirect to a view showing the drug details
    else:
        form = DrugForm()
    return render(request, 'Receipts/add-drug.html', {'form': form})

def add_provision(request):
    if request.method == 'POST':
        form = ProvisionForm(request.POST)
        if form.is_valid():
            provision_name = form.cleaned_data['name']
            # Check if a provision with the same name already exists
            existing_provision = Provision.objects.filter(provision_name__iexact=provision_name).first()
            if existing_provision:
                # If the provision already exists, redirect to a view or page showing the existing provision details
                return redirect('item-details', item_type="Provision", item_id=existing_provision.id)
            else:
                # If the provision does not exist, save the new provision
                form.save()
                return redirect('item-details', item_type="Provision", item_id=existing_provision.id)  # Redirect to a view showing the provision details
    else:
        form = ProvisionForm()
    return render(request, 'Receipts/add-provision.html', {'form': form})


def add_receipt(request):
    if request.method == 'POST':
        receipt_form = ReceiptForm(request.POST)
        receipt_item_formset = ReceiptItemFormSet(request.POST, queryset=ReceiptItem.objects.none())

        if receipt_form.is_valid() and receipt_item_formset.is_valid():
            # Save receipt form data
            receipt = receipt_form.save()

            # Link each item receipt to the main receipt instance
            for form in receipt_item_formset.cleaned_data:
                item = form.get('item')
                quantity_added = form.get('quantity_added')
                cost_price = form.get('cost_price')
                former_quantity = form.get('former_quantity')
                ReceiptItem.objects.create(receipt=receipt, item=item, quantity_added=quantity_added, cost_price=cost_price, former_quantity=former_quantity)

            return redirect('index')  # Redirect to a view showing a list of receipts
    else:
        receipt_form = ReceiptForm()
        receipt_item_formset = ReceiptItemFormSet(queryset=ReceiptItem.objects.none())

    return render(request, 'Receipts/add-receipt.html', {
        'receipt_form': receipt_form,
        'receipt_item_formset': receipt_item_formset
    })

class DrugAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Drug.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)[:10] 
        return qs