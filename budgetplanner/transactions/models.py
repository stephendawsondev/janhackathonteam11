# transactions/models.py
from django.db import models
from accounts.models import User
from django.db.models import Sum
from datetime import datetime, timedelta
from django.utils.timezone import now
from decimal import Decimal


class typicalExpense(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Function to create typical expenses


def create_typical_expenses():
    typicalExpense.objects.create(name='Rent')
    typicalExpense.objects.create(name='Car Insurance')
    typicalExpense.objects.create(name='Groceries')
    typicalExpense.objects.create(name='Utilities')
    typicalExpense.objects.create(name='Health Insurance')
    typicalExpense.objects.create(name='Internet Bill')
    TypicalExpense.objects.create(name='Dining Out')
    TypicalExpense.objects.create(name='Electricity Bill')
    TypicalExpense.objects.create(name='Gas Bill')
    TypicalExpense.objects.create(name='Water Bill')
    TypicalExpense.objects.create(name='Phone Bill')
    TypicalExpense.objects.create(name='Transportation')
    TypicalExpense.objects.create(name='Clothing')
    TypicalExpense.objects.create(name='Entertainment')
    TypicalExpense.objects.create(name='Gym Membership')
    TypicalExpense.objects.create(name='Childcare')
    TypicalExpense.objects.create(name='Education')
    TypicalExpense.objects.create(name='Healthcare')
    TypicalExpense.objects.create(name='Home Repairs')
    TypicalExpense.objects.create(name='Travel')
    TypicalExpense.objects.create(name='Gifts')
    TypicalExpense.objects.create(name='Pet Expenses')
    TypicalExpense.objects.create(name='Charity Donations')
    TypicalExpense.objects.create(name='Hobbies')
    TypicalExpense.objects.create(name='Taxes')
    TypicalExpense.objects.create(name='Insurance Premiums')
    TypicalExpense.objects.create(name='Subscription Services')
    TypicalExpense.objects.create(name='Home Maintenance')


class typicalIncome(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def create_typical_incomes():
    TypicalIncome.objects.create(name='Salary')
    TypicalIncome.objects.create(name='Bonus')


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date = models.DateField()
    typical_income = models.ForeignKey(
        'transactions.TypicalIncome', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s income from {self.source} on {self.date}"



class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.username}'s budget from {self.start_date}"

class WeeklyBudget(Budget):
    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=6)
        super().save(*args, **kwargs)

    def __str__(self):
        return super().__str__() + f" to {self.end_date}"
   

class MonthlyBudget(Budget):
    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return super().__str__() + f" to {self.end_date}"

class YearlyBudget(Budget):
    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=365)
        super().save(*args, **kwargs)

    def __str__(self):
        return super().__str__() + f" to {self.end_date}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=50)
    date = models.DateField()
    typical_expense = models.ForeignKey(
        typicalExpense, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s expense on {self.date}"

def get_income_totals(user):
    today = datetime.today()
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    monthly_total = Income.objects.filter(
        user=user,
        date__gte=start_of_month
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    yearly_total = Income.objects.filter(
        user=user,
        date__gte=start_of_year
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    return {
        'monthly_income_total': monthly_total,
        'yearly_income_total': yearly_total
    }


def get_expense_totals(user):
    current_date = now().date()
    start_of_week = current_date - \
        timedelta(days=current_date.weekday()) + timedelta(days=3)
    start_of_month = current_date.replace(day=1)
    start_of_year = current_date.replace(month=1, day=1)

    if start_of_week > current_date:
        start_of_week -= timedelta(weeks=1)

    weekly_total = Expense.objects.filter(
        user=user, date__gte=start_of_week
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    monthly_total = Expense.objects.filter(
        user=user, date__gte=start_of_month
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    yearly_total = Expense.objects.filter(
        user=user, date__gte=start_of_year
    ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    return {
        'weekly_expense_total': weekly_total,
        'monthly_expense_total': monthly_total,
        'yearly_expense_total': yearly_total
    }
