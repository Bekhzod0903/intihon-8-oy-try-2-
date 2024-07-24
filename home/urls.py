from django.urls import path
from .views import home, IncomeView, ExpenseView,TransactionDeleteView,edit_transaction,set_language

urlpatterns = [
    path('', home, name='home'),
    path('income/', IncomeView.as_view(), name='income'),
    path('expense/', ExpenseView.as_view(), name='expense'),
    path('i18n/setlang/', set_language, name='set_language'),
    path('edit_transaction/<int:transaction_id>/', edit_transaction, name='edit_transaction'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),

]
