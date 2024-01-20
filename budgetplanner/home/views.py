from django.shortcuts import render
from accounts.utils import anonymous_required
from django.contrib import messages
from datetime import datetime
import random


def home(request):
    return render(request, 'home/index.html')

# DEMO: User Dashboard


@anonymous_required('dashboard')
def demo_dashboard_view(request):

    # Income totals
    weekly_income_total = random.randint(1, 100)
    monthly_income_total = random.randint(100, 1000)
    yearly_income_total = random.randint(1000, 10000)

    # Expenditure totals
    weekly_expenditure_total = random.randint(1, 50)
    monthly_expenditure_total = random.randint(50, 500)
    yearly_expenditure_total = random.randint(500, 5000)

    messages.info(
        request, 'This is just a demo version of the User Dashboard. Please log in to utilize the app.')

    context = {
        'weekly_income_total': weekly_income_total,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
        'weekly_expenditure_total': weekly_expenditure_total,
        'monthly_expenditure_total': monthly_expenditure_total,
        'yearly_expenditure_total': yearly_expenditure_total,
    }
    return render(request, 'demo/demo_dashboard.html', context)

@anonymous_required('income')
def demo_income_view(request):
    date = datetime.today()
    source = 'Salary'
    amount = random.randint(1000, 2000)
    monthly_income_total = amount
    yearly_income_total = random.randint(10000, 24000)
    incomes = random.randint(1, 100)

    context = {
        'date': date,
        'source': source,
        'amount': amount,
        'incomes': incomes,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
    }

    return render(request, 'demo/demo_income.html', context)