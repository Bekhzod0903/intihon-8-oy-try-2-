from django.contrib import admin
from .models import Transaction,ExpenseCategory,IncomeCategory,TotalSum
# Register your models here.

admin.site.register(Transaction)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(TotalSum)
