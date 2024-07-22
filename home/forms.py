from django import forms
from .models import IncomeCategory, ExpenseCategory

class IncomeForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=IncomeCategory.objects.all(),
        empty_label="Select Income Category",
        widget=forms.Select(attrs={'class': 'form-select mb-2'})
    )
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter amount'})
    )

class ExpenseForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=ExpenseCategory.objects.all(),
        empty_label="Select Expense Category",
        widget=forms.Select(attrs={'class': 'form-select mb-2'})
    )
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter amount'})
    )
