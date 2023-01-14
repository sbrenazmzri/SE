from django.shortcuts import render, redirect
from .forms import PurchaseOrderForm

def purchase_order(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PurchaseOrderForm()
    return render(request, 'purchase_order.html', {'form': form})

def purchase_order_success(request):
    return render(request, 'purchase_order_success.html')