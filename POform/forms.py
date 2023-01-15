from django import forms
from django.core.validators import MinValueValidator


class EmployeeForm(forms.Form):
    em_id = forms.CharField(label='Employee ID', max_length=10)
    name = forms.CharField(label='Name', max_length=100)
    phone_num = forms.CharField(label='Contact Number', max_length=10)
    email_address = forms.CharField(label='Email Address', max_length=100)
    address = forms.CharField(label='Address', widget=forms.Textarea)

class FinanceOfficerForm(forms.Form):
    fo_id = forms.CharField(label='Finance Officer ID', max_length=10)
    name = forms.CharField(label='Name', max_length=100)
    phone_num = forms.CharField(label='Contact Number', max_length=10)
    address = forms.CharField(label='Address', widget=forms.Textarea)

class SupplierForm(forms.Form):
    su_id = forms.CharField(label='Supplier ID', max_length=10)
    name = forms.CharField(label='Name', max_length=100)
    phone_num = forms.CharField(label='Contact Number', max_length=10)
    address = forms.CharField(label='Address', widget=forms.Textarea)

class ProductForm(forms.Form):
    product_id = forms.CharField(label='Product ID', max_length=10)
    name = forms.CharField(label='Name', max_length=100)
    product_type = forms.CharField(label='Product type', max_length=100)
    price = forms.DecimalField(label='Price (RM)', decimal_places=2, validators=[MinValueValidator(0.0)])
    quantity = forms.IntegerField(label='Quantity')

class PurchaseOrderForm(forms.Form):
    po_id = forms.CharField(label='Product ID', max_length=10)
    ship_to_date = forms.DateField(label='Ship to Date')
    order_date = forms.DateField(label='Order Date')
    ship_to_address = forms.CharField(label='Ship to Address', widget=forms.Textarea)


