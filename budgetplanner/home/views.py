from django.shortcuts import render
from accounts.utils import anonymous_required
from django.contrib import messages
import random

def home(request):
    return render(request, 'home/index.html')

# DEMO: User Dashboard


@anonymous_required('dashboard')
def demo_dashboard_view(request):
    messages.info(
        request, 'This is just a demo version of the User Dashboard. Please log in to utilize the app.')

    indebt = random.randint(1, 100)
    savings = random.randint(100, 500)
    invested = random.randint(100, 500)
    current_balance = invested + savings - indebt
    context = {
        'indebt': indebt,
        'savings': savings,
        'invested': invested,
        'current_balance': current_balance,
    }
    return render(request, 'demo_dashboard.html', context)
