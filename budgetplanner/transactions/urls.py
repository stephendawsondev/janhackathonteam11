from django.urls import path
from . import views

urlpatterns = [
    path('income/', views.income_view, name='income'),
    path('expenditure/', views.expenditure_view, name='expenditure'),
    path('add-expense/', views.add_expense_view, name='add_expense'),
    path('reports/', views.reports_view, name='reports'),
]