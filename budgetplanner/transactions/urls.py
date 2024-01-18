from django.urls import path
from .views import income_view, expenditure_view, add_expense_view, reports_view

urlpatterns = [
    path('income/', income_view, name='income'),
    path('expenditure/', expenditure_view, name='expenditure'),
    path('add-expense/', add_expense_view, name='add_expense'),
    path('reports/', reports_view, name='reports'),
]