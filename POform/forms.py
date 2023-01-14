from django import forms

class PurchaseOrderForm(forms.Form):
    po_number = forms.CharField(label='Purchase Order Number', max_length=20)
    supplier = forms.CharField(label='Supplier', max_length=100)
    ordered_items = forms.CharField(label='Ordered Items', widget=forms.Textarea)
    order_date = forms.DateField(label='Order Date')
    delivery_date = forms.DateField(label='Delivery Date')