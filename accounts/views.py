from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from .forms import UserRegistrationForm
from .models import UserProfile
from transactions.models import Income, Expense, WeeklyBudget, MonthlyBudget, YearlyBudget, Invest
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Custom Register


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been registered!')
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Custom Login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in!')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect(reverse('login'))
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Custom Logout


def logout_view(request):
    messages.info(request,
                  'You have successfully logged out!')
    logout(request)
    return redirect(reverse('home'))

# Custom Password Reset


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

# User Dashboard


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
    # Fetching the latest weekly, monthly, and yearly budgets
    latest_weekly_budget = WeeklyBudget.objects.filter(
        user=request.user).order_by('-start_date').first()
    latest_monthly_budget = MonthlyBudget.objects.filter(
        user=request.user).order_by('-start_date').first()
    latest_yearly_budget = YearlyBudget.objects.filter(
        user=request.user).order_by('-start_date').first()
    user_profile = UserProfile.objects.get(
        user=request.user) if request.user.is_authenticated else None

    context = {
        'user_profile': user_profile,
        'current_balance': user_profile.current_balance() if user_profile else 0,
        'weekly_income_total': weekly_income_total,
        'monthly_income_total': monthly_income_total,
        'yearly_income_total': yearly_income_total,
        'weekly_expenditure_total': weekly_expenditure_total,
        'monthly_expenditure_total': monthly_expenditure_total,
        'yearly_expenditure_total': yearly_expenditure_total,
        'latest_weekly_budget': latest_weekly_budget,
        'latest_monthly_budget': latest_monthly_budget,
        'latest_yearly_budget': latest_yearly_budget,
    }

    return render(request, 'dashboard.html', context)


@login_required
def manage_settings_view(request):
    return render(request, 'manage_settings.html')


@login_required
def update_user_view(request):
    form = UserRegistrationForm(instance=request.user)
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(
            request, 'You have successfully updated your profile!')
        return redirect(reverse('manage_settings'))

    return render(request, 'update_user.html', {'form': form})


def delete_user(request):
    user = request.user
    user.delete()
    messages.success(
        request, 'You have successfully deleted your account!')
    return redirect(reverse('home'))
