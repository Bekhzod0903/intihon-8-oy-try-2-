from django.conf import settings
from django.db import models
# models.py
from django.conf import settings
from django.db import models

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=250, choices=[('Cash', 'Cash'), ('Card', 'Card')])
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

class TotalSum(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


