# transactions/admin.py
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import WeeklyBudget, MonthlyBudget, YearlyBudget, Expense, Income



class ExpenseAdmin(SummernoteModelAdmin):
    list_display = (
        'user',
        'amount',
        'description',
        'date',
        'typical_expense',
    )

    list_filter = ('date', 'typical_expense', )
    search_fields = ['user', 'typical_expense', 'amount', 'description', ]

    summernote_fields = ('description')

    ordering = ('-date',)


class IncomeAdmin(SummernoteModelAdmin):
    list_display = (
        'user',
        'amount',
        'source',
        'date',
        'typical_income',
    )

    list_filter = ('date', 'typical_income', )
    search_fields = ['user', 'typical_income', 'amount', 'source', ]

    summernote_fields = ('source')

    ordering = ('-date',)



admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
