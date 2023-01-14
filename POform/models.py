from django.db import models

class Employee(models.Model):
    em_id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=100)
    phone_num = models.IntegerField(max_length=10)
    email_address = models.CharField(max_length=100)
    address = models.TextField()

class FinanceOfficer(models.Model):
    fo_id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=100)
    phone_num = models.IntegerField(max_length=10)
    email_address = models.CharField(max_length=100)
   