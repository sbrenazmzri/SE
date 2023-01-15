from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Employee)
admin.site.register(FinanceOfficer)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(PurchaseOrder)





