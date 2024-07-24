from django.urls import path
from .views import home, IncomeView, ExpenseView,TransactionDeleteView,edit_transaction,set_theme

urlpatterns = [
    path('', home, name='home'),
    path('income/', IncomeView.as_view(), name='income'),
    path('expense/', ExpenseView.as_view(), name='expense'),
    path('set-theme/<str:theme>/', set_theme, name='set_theme'),
    path('edit_transaction/<int:transaction_id>/', edit_transaction, name='edit_transaction'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),

]
