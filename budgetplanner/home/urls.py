# Django Imports
from django.urls import path
from .views import home, demo_dashboard_view

urlpatterns = [
    path('', home, name='home'),
    path('demo/', demo_dashboard_view, name='demo_dashboard'),
]
