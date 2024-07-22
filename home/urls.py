from django.urls import path
from .views import home, IncomeView, ExpenseView

urlpatterns = [
    path('', home, name='home'),
    path('income/', IncomeView.as_view(), name='income'),
    path('expense/', ExpenseView.as_view(), name='expense'),
]
