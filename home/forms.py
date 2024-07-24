from django.utils.translation import gettext_lazy as _
from .models import IncomeCategory, ExpenseCategory
from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'payment_method', 'category', 'transaction_type']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount and (amount.as_tuple().exponent < -2):
            raise forms.ValidationError("Ensure that there are no more than 2 decimal places.")
        return amount


class IncomeForm(forms.Form):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
    ]

    category = forms.ModelChoiceField(
        queryset=IncomeCategory.objects.all(),
        empty_label="Select Income Category",
        widget=forms.Select(attrs={'class': 'form-select mb-2'})
    )
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter amount'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select mb-2', 'id': 'payment-method'})
    )
    bank_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter bank name'}),
        label='Bank Name'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initializing JavaScript for dynamic field display
        self.fields['payment_method'].widget.attrs.update({'onchange': 'toggleBankNameField()'})


class ExpenseForm(forms.Form):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
    ]

    category = forms.ModelChoiceField(
        queryset=ExpenseCategory.objects.all(),
        empty_label="Select Expense Category",
        widget=forms.Select(attrs={'class': 'form-select mb-2'})
    )
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter amount'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select mb-2', 'id': 'payment-method'})
    )
    bank_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter bank name'}),
        label='Bank Name'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initializing JavaScript for dynamic field display
        self.fields['payment_method'].widget.attrs.update({'onchange': 'toggleBankNameField()'})


class NewIncomeCategoryForm(forms.ModelForm):
    class Meta:
        model = IncomeCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter new income category'})
        }


class NewExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter new expense category'})
        }




class LanguageForm(forms.Form):
    language = forms.ChoiceField(
        choices=[('uz', _('Uzbek')), ('ru', _('Russian')), ('en', _('English'))],
        label=_('Choose Language'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )