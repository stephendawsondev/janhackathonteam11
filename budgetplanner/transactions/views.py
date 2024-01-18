from django.shortcuts import render

def income_view(request):
    return render(request, 'transactions/income.html')

def expenditure_view(request):
    return render(request, 'transactions/expenditure.html')

def reports_view(request):
    return render(request, 'transactions/reports.html')

# Create your views here.
