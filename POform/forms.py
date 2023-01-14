from django import forms

class EmployeeForm(forms.Form):
    em_id = forms.CharField(label='Employee ID', max_length=10)
    name = forms.CharField(label='Name', max_length=100)
    phone_num = forms.CharField(label='Contact Number', max_length=10)
    email_address = forms.CharField(label='Name', max_length=100)
    address = forms.DateField(label='Address', widget=forms.Textarea)

class FinanceOfficerForm(forms.Form):
    fo_id = forms.CharField(label='Finance Officer ID', max_length=10)
    name = forms.CharField(label='Name', max_length=100)
    phone_num = forms.CharField(label='Contact Number', max_length=10)
    address = forms.DateField(label='Address', widget=forms.Textarea)