from django.shortcuts import render
from accounts.utils import anonymous_required
from django.contrib import messages
from datetime import datetime, timedelta
import random
from django.utils.timezone import now
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


def demo_expenditure_view(request):

    expenses = random.randint(1000, 2000)
    datewise_totals = expenses

    # Get current date and calculate the start of the week, month, and year
    current_date = now().date()
    start_of_week = current_date - \
        timedelta(days=current_date.weekday()) + timedelta(days=3)
    start_of_month = current_date.replace(day=1)
    start_of_year = current_date.replace(month=1, day=1)

    # Adjust the start_of_week if it's in the future
    if start_of_week > current_date:
        start_of_week -= timedelta(weeks=1)

    weekly_totals = random.randint(1000, 2000)
    monthly_totals = random.randint(1000, 2000)
    yearly_totals = random.randint(1000, 2000)

    # Calculate daily totals for the current week
    daily_totals = []
    for i in range(7):
        day = start_of_week + timedelta(days=i)
        total = random.randint(1000, 2000)
        daily_totals.append({'day': day, 'total': total})

    context = {
        'demo_expenses': expenses,
        'demo_datewise_totals': datewise_totals,
        'demo_weekly_totals': weekly_totals,
        'demo_monthly_totals': monthly_totals,
        'demo_yearly_totals': yearly_totals,
        'demo_daily_totals': daily_totals,
    }

    return render(request, 'demo/demo_expenditure.html', context)
