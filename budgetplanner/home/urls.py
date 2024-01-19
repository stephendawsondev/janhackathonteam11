# Django Imports
from django.urls import path
from .views import home, demo_dashboard_view, demo_income_view

urlpatterns = [
    path('', home, name='home'),
    path('demo/', demo_dashboard_view, name='demo_dashboard'),
    path('demo/income', demo_income_view, name='demo_income'),
]
