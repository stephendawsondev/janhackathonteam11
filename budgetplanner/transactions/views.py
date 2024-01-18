from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import ExpenseForm
from .models import Expense
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def income_view(request):
    return render(request, 'transactions/income.html')

@login_required
def expenditure_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenditure')  # Redirect back to the expenditure page to show the new expense
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    datewise_totals = Expense.objects.filter(user=request.user)\
                                     .values('date')\
                                     .annotate(total=Sum('amount'))\
                                     .order_by('-date')

    context = {
        'form': form,
        'expenses': expenses,
        'datewise_totals': datewise_totals,
    }
    return render(request, 'transactions/expenditure.html', context)
# views.py
@login_required
def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenditure')  # Redirect to the expenditure view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ExpenseForm()
    
    # If not POST or form not valid, just show the form again
    return render(request, 'transactions/add_expense_form.html', {'form': form})
def reports_view(request):
    return render(request, 'transactions/reports.html')

# Create your views here.
