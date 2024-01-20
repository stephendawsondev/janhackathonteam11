# transactions/admin.py
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import WeeklyBudget, MonthlyBudget, YearlyBudget, Expense, Income, ExpenseCategory, IncomeCategory


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    search_fields = ['name', ]

    class Meta:
        verbose_name_plural = 'Expense Categories'

    def __str__(self):
        return self.name


class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    search_fields = ['name', ]

    class Meta:
        verbose_name_plural = 'Income Categories'

    def __str__(self):
        return self.name


class ExpenseAdmin(SummernoteModelAdmin):
    list_display = (
        'user',
        'amount',
        'description',
        'date',
        'category',
    )

    list_filter = ('date', )
    search_fields = ['user', 'amount', 'description', ]

    summernote_fields = ('description')

    ordering = ('-date',)


class IncomeAdmin(SummernoteModelAdmin):
    list_display = (
        'user',
        'amount',
        'source',
        'date',
        'category',
    )

    list_filter = ('date', 'category')
    search_fields = ['user', 'category', 'amount', 'source', ]

    summernote_fields = ('source')

    ordering = ('-date',)


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(IncomeCategory, IncomeCategoryAdmin)

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
