from django.shortcuts import render
from accounts.utils import anonymous_required
from django.contrib import messages
from datetime import datetime
import random
from demo.views import (demo_dashboard_view, demo_income_view, demo_expenditure_view, demo_manage_budgets)

def home(request):
    return render(request, 'home/index.html')
