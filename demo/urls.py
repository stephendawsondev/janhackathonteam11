# Django Imports
from django.urls import path
from .views import (demo_dashboard_view, demo_income_view,
                    demo_expenditure_view, demo_manage_budgets)

urlpatterns = [
    path('demo/', demo_dashboard_view, name='demo_dashboard'),
    path('demo/income', demo_income_view, name='demo_income'),
    path('demo/expenditure', demo_expenditure_view, name='demo_expenditure_view'),
    path('demo/manage_budgets', demo_manage_budgets, name='demo_manage_budgets'),


]
