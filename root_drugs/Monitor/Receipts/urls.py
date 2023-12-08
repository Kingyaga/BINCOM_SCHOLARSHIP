from django.urls import path
from . import views

app_name= "Receipts"
urlpatterns = [
    path("", views.index, name= "index"),
    path("suppliers/", views.supplier_list, name= "supplier-list"),
    path('suppliers/<int:supplier_id>/', views.supplier_details, name='supplier-details'),
    path('drug/<int:drug_id>/', views.drug_details, name='drug-details'),
    path('search/', views.search_drug_history, name='search-drug'),
    path('receipt/<int:supplier_id>/', views.receipt, name='receipt'),
    path('Details/<int:supply_id>/', views.Receipt_details, name='Receipt_details'),
    path('New-receipt/', views.add_receipt, name='add-receipt'),
    path('New-supplier/', views.add_supplier, name='add-supplier'),
    path('New-drug/', views.add_drug, name='add-drug'),
    path('product-autocomplete/', views.ProductAutocomplete.as_view(), name='product-autocomplete')
] 