from django.urls import path
from .views import income_view, expenditure_view, reports_view
from . import views
urlpatterns = [
    path('income/', income_view, name='income'),
    path('expenditure/', expenditure_view, name='expenditure'),
    path('reports/', reports_view, name='reports'),
     path('manage_budgets/', views.manage_budgets, name='manage_budgets'),
     path('expenses/update/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
      path('incomes/update/<int:income_id>/', views.update_income, name='update_income'),
    path('incomes/delete/<int:income_id>/', views.delete_income, name='delete_income'),
]
