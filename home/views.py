from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Transaction, TotalSum, IncomeCategory, ExpenseCategory
from .forms import IncomeForm, ExpenseForm
from decimal import Decimal, InvalidOperation
@login_required
def home(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    total_sum = sum(t.amount if t.transaction_type == 'income' else -t.amount for t in transactions)

    if request.method == 'POST':
        if 'income_submit' in request.POST:
            form = IncomeForm(request.POST)
            if form.is_valid():
                category = form.cleaned_data['category']
                amount = form.cleaned_data['amount']
                Transaction.objects.create(
                    user=request.user,
                    amount=amount,
                    category=category.name,
                    transaction_type='income'
                )
                update_total_sum(request.user)
                return redirect('home')
        elif 'expense_submit' in request.POST:
            form = ExpenseForm(request.POST)
            if form.is_valid():
                category = form.cleaned_data['category']
                amount = form.cleaned_data['amount']
                Transaction.objects.create(
                    user=request.user,
                    amount=amount,
                    category=category.name,
                    transaction_type='expense'
                )
                update_total_sum(request.user)
                return redirect('home')

    return render(request, 'home.html', {'total_sum': total_sum, 'transactions': transactions})

def update_total_sum(user):
    transactions = Transaction.objects.filter(user=user)
    total_sum = sum(t.amount if t.transaction_type == 'income' else -t.amount for t in transactions)
    total_sum_obj, created = TotalSum.objects.get_or_create(user=user)
    total_sum_obj.total_sum = total_sum
    total_sum_obj.save()

class IncomeView(View):
    def get(self, request, *args, **kwargs):
        form = IncomeForm()
        return render(request, 'income.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IncomeForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            Transaction.objects.create(
                user=request.user,
                amount=amount,
                category=category.name,
                transaction_type='income'
            )
            update_total_sum(request.user)
            return redirect('home')
        return render(request, 'income.html', {'form': form})

class ExpenseView(View):
    def get(self, request, *args, **kwargs):
        form = ExpenseForm()
        return render(request, 'expense.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            Transaction.objects.create(
                user=request.user,
                amount=amount,
                category=category.name,
                transaction_type='expense'
            )
            update_total_sum(request.user)
            return redirect('home')
        return render(request, 'expense.html', {'form': form})
