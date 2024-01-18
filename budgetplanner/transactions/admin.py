# transactions/admin.py
from django.contrib import admin
from .models import Budget, Expense, Income

admin.site.register(Budget)
admin.site.register(Expense)
admin.site.register(Income)

# Register your models here.
