from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from .forms import UserRegistrationForm
from .models import UserProfile
from transactions.models import Income,Expense
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from transactions.models import get_income_totals, get_expense_totals

from django.contrib.auth import authenticate, login

def homepage_view(request):
    return render(request,'homepage.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        # Get username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to the dashboard view
            return redirect(reverse('homepage'))
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # Render the login form template if not a POST request
        return render(request, 'login.html')


def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='registration/password_reset_email.html',
                subject_template_name='registration/password_reset_subject.txt'
            )

            # In preparation for when we add toast messages
            messages.success(
                request, 'Instructions to reset your password have been sent to your email.')
            messages.error(
                request, 'An error occurred while sending the email. Please try again later.')

            return redirect(reverse('login'))
    else:
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})


@login_required
def dashboard_view(request):
    current_date = now().date()
    start_of_week = current_date - timedelta(days=current_date.weekday())
    start_of_month = current_date.replace(day=1)
    start_of_year = current_date.replace(month=1, day=1)

    # Income totals
    weekly_income_total = Income.objects.filter(
        user=request.user, 
        date__gte=start_of_week
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    monthly_income_total = Income.objects.filter(
        user=request.user, 
        date__gte=start_of_month
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    yearly_income_total = Income.objects.filter(
        user=request.user, 
        date__gte=start_of_year
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    # Expenditure totals
    weekly_expenditure_total = Expense.objects.filter(
        user=request.user, 
        date__gte=start_of_week
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    monthly_expenditure_total = Expense.objects.filter(
        user=request.user, 
        date__gte=start_of_month
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    yearly_expenditure_total = Expense.objects.filter(
        user=request.user, 
        date__gte=start_of_year
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    user_profile = UserProfile.objects.get(user=request.user) if request.user.is_authenticated else None

    context = {
        'user_profile': user_profile,
        'current_balance': user_profile.current_balance() if user_profile else 0,
        'weekly_income_total': weekly_income_total,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
        'weekly_expenditure_total': weekly_expenditure_total,
        'monthly_expenditure_total': monthly_expenditure_total,
        'yearly_expenditure_total': yearly_expenditure_total,
    }

    return render(request, 'dashboard.html', context)
