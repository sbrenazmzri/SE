from django.db import models

class PurchaseOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    order_items = models.TextField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)