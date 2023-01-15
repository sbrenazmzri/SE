from django.urls import path
from . import views

urlpatterns = [
    path('POform/Employee_Page/', views.employee, name='Employee_Page'),
    path('POform/FinanceOfficer_Page/', views.finance_officer, name='FinanceOfficer_Page'),
    path('POform/Supplier_Page/', views.supplier, name='Supplier_Page'),
    path('POform/Product/', views.product, name='Product_Page'),
    path('POform/Purchase_Order_Page/', views.purchase_order, name='Purchase_Order_Page'),
    path('POform/success/', views.purchase_order_success, name='success')
]