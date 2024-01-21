# Django Imports
from django.urls import path
from .views import demo_dashboard_view, demo_income_view, demo_expenditure_view

urlpatterns = [
    path('demo/', demo_dashboard_view, name='demo_dashboard'),
    path('demo/income', demo_income_view, name='demo_income'),
    path('demo/expenditure', demo_expenditure_view, name='demo_expenditure'),

]
