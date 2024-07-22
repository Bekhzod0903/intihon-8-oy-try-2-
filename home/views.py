from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Transaction, TotalSum, IncomeCategory, ExpenseCategory
from .forms import IncomeForm, ExpenseForm, NewIncomeCategoryForm, NewExpenseCategoryForm
from datetime import datetime, timedelta

@login_required
def home(request):
    transactions = Transaction.objects.filter(user=request.user)
    total_sum = sum(t.amount if t.transaction_type == 'income' else -t.amount for t in transactions)

    # Filtering logic
    filter_type = request.GET.get('filter', 'all')
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    if filter_type == 'today':
        transactions = transactions.filter(date__date=today)
    elif filter_type == 'yesterday':
        transactions = transactions.filter(date__date=yesterday)
    elif filter_type == 'week':
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        transactions = transactions.filter(date__date__range=[start_week, end_week])
    elif filter_type == 'month':
        transactions = transactions.filter(date__year=today.year, date__month=today.month)
    elif filter_type == 'year':
        transactions = transactions.filter(date__year=today.year)

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

    return render(request, 'home.html', {
        'total_sum': total_sum,
        'transactions': transactions,
        'filter_type': filter_type
    })

def update_total_sum(user):
    transactions = Transaction.objects.filter(user=user)
    total_sum = sum(t.amount if t.transaction_type == 'income' else -t.amount for t in transactions)
    total_sum_obj, created = TotalSum.objects.get_or_create(user=user)
    total_sum_obj.total_sum = total_sum
    total_sum_obj.save()

class IncomeView(View):
    def get(self, request, *args, **kwargs):
        form = IncomeForm()
        new_category_form = NewIncomeCategoryForm()
        return render(request, 'income.html', {'form': form, 'new_category_form': new_category_form})

    def post(self, request, *args, **kwargs):
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
        elif 'new_income_category' in request.POST:
            new_category_form = NewIncomeCategoryForm(request.POST)
            if new_category_form.is_valid():
                new_category_form.save()
                return redirect('income')
        form = IncomeForm()
        new_category_form = NewIncomeCategoryForm()
        return render(request, 'income.html', {'form': form, 'new_category_form': new_category_form})

class ExpenseView(View):
    def get(self, request, *args, **kwargs):
        form = ExpenseForm()
        new_category_form = NewExpenseCategoryForm()
        return render(request, 'expense.html', {'form': form, 'new_category_form': new_category_form})

    def post(self, request, *args, **kwargs):
        if 'expense_submit' in request.POST:
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
        elif 'new_expense_category' in request.POST:
            new_category_form = NewExpenseCategoryForm(request.POST)
            if new_category_form.is_valid():
                new_category_form.save()
                return redirect('expense')
        form = ExpenseForm()
        new_category_form = NewExpenseCategoryForm()
        return render(request, 'expense.html', {'form': form, 'new_category_form': new_category_form})
