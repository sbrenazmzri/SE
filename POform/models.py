from django.db import models
from django.core.validators import MinValueValidator

class Employee(models.Model):
    em_id = models.IntegerField()
    name = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    email_address = models.CharField(max_length=100)
    address = models.TextField()

class FinanceOfficer(models.Model):
    fo_id = models.IntegerField()
    name = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    email_address = models.CharField(max_length=100)

class Supplier(models.Model):
    su_id = models.IntegerField()
    name = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    email_address = models.CharField(max_length=100)

class Product(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2,validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField()

class PurchaseOrder(models.Model):
    po_id = models.CharField(max_length=10)
    ship_to_date = models.DateField()
    order_date = models.DateField()  
    ship_to_address = models.TextField()
