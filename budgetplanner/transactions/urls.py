from django.urls import path
from .views import income_view, expenditure_view, reports_view

urlpatterns = [
    path('income/', income_view, name='income'),
    path('expenditure/', expenditure_view, name='expenditure'),
    path('reports/', reports_view, name='reports'),
]
