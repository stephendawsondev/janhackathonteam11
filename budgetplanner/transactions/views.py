from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income
from datetime import datetime, timedelta
from datetime import date
from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from .models import WeeklyBudget, MonthlyBudget, YearlyBudget
from .forms import WeeklyBudgetForm, MonthlyBudgetForm, YearlyBudgetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.forms.widgets import SelectDateWidget
@login_required
def update_budget(request, budget_id, budget_type):
    BudgetModel = {
        'weekly': WeeklyBudget,
        'monthly': MonthlyBudget,
        'yearly': YearlyBudget
    }.get(budget_type)

    budget = get_object_or_404(BudgetModel, id=budget_id, user=request.user)

    if request.method == 'POST':
        form = {
            'weekly': WeeklyBudgetForm,
            'monthly': MonthlyBudgetForm,
            'yearly': YearlyBudgetForm
        }.get(budget_type)(request.POST, instance=budget)

        if form.is_valid():
            form.save()
            messages.success(request, f'{budget_type.capitalize()} budget updated successfully!')
            return redirect('manage_budgets')
    else:
        form = {
            'weekly': WeeklyBudgetForm,
            'monthly': MonthlyBudgetForm,
            'yearly': YearlyBudgetForm
        }.get(budget_type)(instance=budget)

    return render(request, 'transactions/update_budget.html', {'form': form, 'budget_type': budget_type})

@login_required
def manage_budgets(request):
    user = request.user

    weekly_budgets = WeeklyBudget.objects.filter(user=user)
    monthly_budgets = MonthlyBudget.objects.filter(user=user)
    yearly_budgets = YearlyBudget.objects.filter(user=user)

    if request.method == 'POST':
        # Handling Weekly Budget Form
        if 'weekly_budget' in request.POST:
            weekly_form = WeeklyBudgetForm(request.POST)
            if weekly_form.is_valid():
                start_date = weekly_form.cleaned_data['start_date']
                # Ensure there's no overlapping weekly budget
                if not WeeklyBudget.objects.filter(user=user, start_date=start_date).exists():
                    weekly_budget = weekly_form.save(commit=False)
                    weekly_budget.user = user
                    weekly_budget.save()
                    messages.success(request, 'Weekly budget created successfully!')
                else:
                    messages.error(request, 'A weekly budget for this period already exists.')
            else:
                messages.error(request, 'Please correct the errors in the weekly budget form.')

        # Handling Monthly Budget Form
        if 'monthly_budget' in request.POST:
            monthly_form = MonthlyBudgetForm(request.POST)
            if monthly_form.is_valid():
                start_date = monthly_form.cleaned_data['start_date']
                # Ensure there's no overlapping monthly budget
                if not MonthlyBudget.objects.filter(user=user, start_date=start_date).exists():
                    monthly_budget = monthly_form.save(commit=False)
                    monthly_budget.user = user
                    monthly_budget.save()
                    messages.success(request, 'Monthly budget created successfully!')
                else:
                    messages.error(request, 'A monthly budget for this period already exists.')
            else:
                messages.error(request, 'Please correct the errors in the monthly budget form.')

        # Handling Yearly Budget Form
        if 'yearly_budget' in request.POST:
            yearly_form = YearlyBudgetForm(request.POST)
            if yearly_form.is_valid():
                start_date = yearly_form.cleaned_data['start_date']
                # Ensure there's no overlapping yearly budget
                if not YearlyBudget.objects.filter(user=user, start_date=start_date).exists():
                    yearly_budget = yearly_form.save(commit=False)
                    yearly_budget.user = user
                    yearly_budget.save()
                    messages.success(request, 'Yearly budget created successfully!')
                else:
                    messages.error(request, 'A yearly budget for this period already exists.')
            else:
                messages.error(request, 'Please correct the errors in the yearly budget form.')
        return redirect('manage_budgets')

    else:
        weekly_form = WeeklyBudgetForm()
        monthly_form = MonthlyBudgetForm()
        yearly_form = YearlyBudgetForm()

    context = {
        'weekly_budgets': weekly_budgets,
        'monthly_budgets': monthly_budgets,
        'yearly_budgets': yearly_budgets,
        'weekly_form': weekly_form,
        'monthly_form': monthly_form,
        'yearly_form': yearly_form,
    }
    return render(request, 'transactions/manage_budgets.html', context)
def calculate_start_date():
    # Calculate the start date (Thursday of the current week)
    current_date = now().date()
    start_date = current_date + timedelta((3 - current_date.weekday() + 7) % 7)
    return start_date

def handle_budget_update_delete(request, budget_id, BudgetModel, budget_form, budget_type):
    budget_instance = get_object_or_404(BudgetModel, id=budget_id, user=request.user)
    if 'update_' + budget_type in request.POST:
        budget_form = budget_form.__class__(request.POST, instance=budget_instance)
        if budget_form.is_valid():
            budget_form.save()
            messages.success(request, f'{budget_type.capitalize()} budget updated successfully!')
    elif 'delete_' + budget_type in request.POST:
        budget_instance.delete()
        messages.success(request, f'{budget_type.capitalize()} budget deleted successfully!')
    return redirect('manage_budgets')
@login_required
def income_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, 'Income added successfully!')
            return redirect('income')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = IncomeForm()

    # Calculate totals similarly as we did for expenses
    today = datetime.today()
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    monthly_income_total = Income.objects.filter(
        user=request.user,
        date__gte=start_of_month
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    yearly_income_total = Income.objects.filter(
        user=request.user,
        date__gte=start_of_year
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    incomes = Income.objects.filter(user=request.user).order_by('-date')
    datewise_totals = incomes.values('date').annotate(
        total=Sum('amount')).order_by('-date')

    context = {
        'form': form,
        'incomes': incomes,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
    }

    return render(request, 'transactions/income.html', context)


@login_required
def expenditure_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenditure')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    datewise_totals = expenses.values('date').annotate(
        total=Sum('amount')).order_by('-date')

    # Get current date and calculate the start of the week, month, and year
    current_date = now().date()
    start_of_week = current_date - \
        timedelta(days=current_date.weekday()) + timedelta(days=3)
    start_of_month = current_date.replace(day=1)
    start_of_year = current_date.replace(month=1, day=1)

    # Adjust the start_of_week if it's in the future
    if start_of_week > current_date:
        start_of_week -= timedelta(weeks=1)

    # Aggregate expenses
    weekly_totals = expenses.filter(
        date__gte=start_of_week).aggregate(weekly_total=Sum('amount'))
    monthly_totals = expenses.filter(
        date__gte=start_of_month).aggregate(monthly_total=Sum('amount'))
    yearly_totals = expenses.filter(
        date__gte=start_of_year).aggregate(yearly_total=Sum('amount'))

    # Calculate daily totals for the current week
    daily_totals = []
    for i in range(7):
        day = start_of_week + timedelta(days=i)
        total = expenses.filter(date=day).aggregate(
            total=Sum('amount'))['total'] or 0
        daily_totals.append({'day': day, 'total': total})

    context = {
        'form': form,
        'expenses': expenses,
        'datewise_totals': datewise_totals,
        'weekly_totals': weekly_totals,
        'monthly_totals': monthly_totals,
        'yearly_totals': yearly_totals,
        'daily_totals': daily_totals,
    }

    return render(request, 'transactions/expenditure.html', context)

# views.py
@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expenditure')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'transactions/update_expense.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('expenditure')
    return render(request, 'transactions/delete_expense.html', {'expense': expense})

def reports_view(request):
    return render(request, 'transactions/reports.html')

# Create your views here.
@login_required
def update_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income updated successfully!')
            return redirect('income')  # Replace with your view name
    else:
        form = IncomeForm(instance=income)
    return render(request, 'transactions/update_income.html', {'form': form})

@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    if request.method == 'POST':
        income.delete()
        messages.success(request, 'Income deleted successfully!')
        return redirect('income')  # Replace with your view name
    return render(request, 'transactions/delete_income.html', {'income': income})