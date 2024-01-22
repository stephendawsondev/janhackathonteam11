from django.shortcuts import render
from accounts.utils import anonymous_required
from django.contrib import messages
from datetime import datetime, timedelta
import random
from django.utils.timezone import now
# DEMO: User Dashboard


@anonymous_required('dashboard')
def demo_dashboard_view(request):
    date = datetime.today()
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
        'demo_start_date': date,
        'demo_weekly_income_total': weekly_income_total,
        'demo_monthly_income_total': monthly_income_total,
        'demo_yearly_income_total': yearly_income_total,
        'demo_weekly_expenditure_total': weekly_expenditure_total,
        'demo_monthly_expenditure_total': monthly_expenditure_total,
        'demo_yearly_expenditure_total': yearly_expenditure_total,
        'latest_weekly_budget': True,
        'latest_monthly_budget': True,
        'latest_yearly_budget': True,
    }
    return render(request, 'demo/demo_dashboard.html', context)


@anonymous_required('income')
def demo_income_view(request):
    date = datetime.today()
    source = 'Salary'

    weekly_income_total = random.randint(500, 1000)
    amount = random.randint(1000, 2000)
    monthly_income_total = amount
    yearly_income_total = random.randint(10000, 24000)
    incomes = random.randint(1, 100)

    context = {
        'date': date,
        'source': source,
        'amount': amount,
        'incomes': incomes,
        'weekly_income_total': weekly_income_total,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
    }

    return render(request, 'demo/demo_income.html', context)


@anonymous_required('expenditure')
def demo_expenditure_view (request):
    date = datetime.today()
    source = 'Salary'
    weekly_income_total = random.randint(500, 1000)
    amount = random.randint(1000, 2000)
    monthly_income_total = amount
    yearly_income_total = random.randint(10000, 24000)
    incomes = random.randint(1, 100)

    context = {
        'date': date,
        'source': source,
        'amount': amount,
        'incomes': incomes,
        'weekly_income_total': weekly_income_total,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
    }

    return render(request, 'demo/demo_expenditure.html', context)


@anonymous_required('manage_budgets')
def demo_manage_budgets_view(request):
    date = datetime.today()
    amount = random.randint(1000, 2000)
    weekly_budgets = random.randint(1000, 2000)
    monthly_budgets = random.randint(1000, 2000)
    yearly_budgets = random.randint(1000, 20000)

    context = {
        'amount': amount,
        'description': 'Demo',
        'date': date,
        'weekly_budgets': weekly_budgets,
        'monthly_budgets': monthly_budgets,
        'yearly_budgets': yearly_budgets,
    }
    return render(request, 'demo/demo_manage_budgets.html', context)
