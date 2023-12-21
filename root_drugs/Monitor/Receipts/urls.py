from django.urls import path
from . import views

app_name= "Receipts"
urlpatterns = [
    path("", views.index, name= "index"),
    path("suppliers/", views.supplier_list, name= "supplier-list"),
    path('suppliers/<int:supplier_id>/', views.supplier_details, name='supplier-details'),
    path('item-details/<str:item_type>/<int:item_id>/', views.item_details, name='item-details'),
    path('search/', views.search_item_history, name='search-items'),
    path('receipt/<int:receipt_id>/', views.receipt, name='receipt'),
    path('Details/<str:item_type>/<int:item_id>/<int:receipt_id>/', views.Receipt_details, name='Receipt_details'),
    path('Add-receipt/', views.add_receipt, name='add-receipt'),
    path('Add-supplier/', views.add_supplier, name='add-supplier'),
    path('Add-drug/', views.add_drug, name='add-drug'),
    path('Add-provision/', views.add_provision, name='add-provision'),
    path('autocomplete/', views.DrugAutocomplete.as_view(), name='autocomplete')
] 