# transactions/models.py
from django.db import models
from accounts.models import User

class TypicalExpense(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Function to create typical expenses
def create_typical_expenses():
    TypicalExpense.objects.create(name='Rent')
    TypicalExpense.objects.create(name='Car Insurance')
    TypicalExpense.objects.create(name='Groceries')
    TypicalExpense.objects.create(name='Utilities')
    TypicalExpense.objects.create(name='Health Insurance')
    TypicalExpense.objects.create(name='Internet Bill')
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





class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s budget from {self.start_date} to {self.end_date}"

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=50)
    date = models.DateField()
    typical_expense = models.ForeignKey(TypicalExpense, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s expense on {self.date}"
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s income on {self.date}"