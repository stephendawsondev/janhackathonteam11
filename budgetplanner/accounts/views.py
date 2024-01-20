from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from .forms import UserRegistrationForm
from .models import UserProfile
from transactions.models import Income, Expense,WeeklyBudget, MonthlyBudget, YearlyBudget
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from transactions.models import get_income_totals, get_expense_totals
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

# Custom Register


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


class LoginView(LoginView):
    """
    LoginView is class based and automatically allows
    the form to be populated in the template.
    """
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have logged in!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard')


# Custom Logout


def logout_view(request):
    messages.info(request,
                  'You have successfully logged out!')
    logout(request)
    return redirect('home')

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
    latest_weekly_budget = WeeklyBudget.objects.filter(user=request.user).order_by('-start_date').first()
    latest_monthly_budget = MonthlyBudget.objects.filter(user=request.user).order_by('-start_date').first()
    latest_yearly_budget = YearlyBudget.objects.filter(user=request.user).order_by('-start_date').first()
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
