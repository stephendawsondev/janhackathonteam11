# Django Imports
from django.urls import path
from .views import home
from demo.views import (demo_dashboard_view, demo_income_view,
                    demo_expenditure_view, demo_manage_budgets)
urlpatterns = [
    path('', home, name='home'),
]
