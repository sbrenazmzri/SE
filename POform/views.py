from django.shortcuts import render, redirect
from .forms import EmployeeForm, FinanceOfficerForm

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EmployeeForm()
    return render(request, 'Employee_details_page.html', {'form': form})

def purchase_order_success(request):
    return render(request, 'Employee_details_page.html')

def finance_officer(request):
    if request.method == 'POST':
        form = FinanceOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FinanceOfficerForm()
    return render(request, 'FinanceOfficer_details_page.html', {'form': form})

def purchase_order_success(request):
    return render(request, 'purchase_order_success.html')