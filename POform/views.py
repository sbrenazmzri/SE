from django.shortcuts import render, redirect
from .forms import EmployeeForm, FinanceOfficerForm, SupplierForm, ProductForm, PurchaseOrderForm

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FinanceOfficer_Page')
    else:
        form = EmployeeForm()
    return render(request, 'Employee_details_page.html', {'form': form})


def finance_officer(request):
    if request.method == 'POST':
        form = FinanceOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Supplier_Page')
    else:
        form = FinanceOfficerForm()
    return render(request, 'FinanceOfficer_details_page.html', {'form': form})

def supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Product_Page')
    else:
        form = SupplierForm()
    return render(request, 'Supplier_details.html', {'form': form})

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Success')
    else:
        form = ProductForm()
    return render(request, 'Product_details.html', {'form': form})

def purchase_order(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Success')
    else:
        form = PurchaseOrderForm()
    return render(request, 'Purchase_Order_details.html', {'form': form})


def purchase_order_success(request):
    return render(request, 'purchase_order_success.html')