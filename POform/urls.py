from django.urls import path
from . import views

urlpatterns = [
    path('POform/Employee_Page/', views.employee, name='Employee_Page'),
    path('POform/FinanceOfficer_Page/', views.finance_officer, name='FinanceOfficer_Page'),
    path('POform/success/', views.purchase_order_success, name='success')
]