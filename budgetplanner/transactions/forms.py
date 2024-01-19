from django import forms
from datetime import date, timedelta
from .models import MonthlyBudget,WeeklyBudget,YearlyBudget
from .models import Expense, typicalExpense, Income, typicalIncome
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.forms.widgets import HiddenInput
from django.forms import SelectDateWidget
from django.utils.timezone import now
from datetime import datetime

def calculate_start_date():
    # Calculate the start date (Thursday of the current week)
    current_date = date.today()
    start_date = current_date + timedelta((3 - current_date.weekday() + 7) % 7)
    return start_date

class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0,
        help_text='Enter a positive amount. Only two decimal places are allowed.',
        widget=forms.NumberInput(attrs={'step': '0.01'})
    )
    description = forms.CharField(
        max_length=50,
        help_text='Maximum 50 characters.',
        widget=forms.TextInput(attrs={'placeholder': 'Description'})
    )

    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date', 'typical_expense']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['typical_expense'].queryset = typicalExpense.objects.all()
        self.fields['typical_expense'].empty_label = "Select a typical expense"

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount and amount.as_tuple().exponent < -2:
            raise ValidationError(
                'Enter an amount with up to two decimal places.')
        return amount


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0,
        help_text='Enter a positive amount. Only two decimal places are allowed.',
        widget=forms.NumberInput(attrs={'step': '0.01'})
    )
    source = forms.CharField(
        max_length=100,
        help_text='Enter the source of the income.',
        widget=forms.TextInput(attrs={'placeholder': 'Source'})
    )

    class Meta:
        model = Income
        fields = ['amount', 'source', 'date', 'typical_income']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['typical_income'].queryset = typicalIncome.objects.all()
        self.fields['typical_income'].empty_label = "Select a typical income"

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError("The amount cannot be negative.")
        return amount

class WeeklyBudgetForm(forms.ModelForm):
    class Meta:
        model = WeeklyBudget
        fields = ['amount', 'start_date']
        widgets = {
            'start_date': SelectDateWidget()
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        if start_date:
            # Calculate the end date as 6 days after the start date
            end_date = start_date + timedelta(days=6)
            cleaned_data['end_date'] = end_date
        return cleaned_data

class MonthlyBudgetForm(forms.ModelForm):
    class Meta:
        model = MonthlyBudget
        fields = ['amount', 'start_date']
        widgets = {
            'start_date': SelectDateWidget()
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        if start_date:
            # Calculate the end date as the last day of the same month
            end_date = start_date + timedelta(days=30)
            cleaned_data['end_date'] = end_date
        return cleaned_data

class YearlyBudgetForm(forms.ModelForm):
    class Meta:
        model = YearlyBudget
        fields = ['amount', 'start_date']
        widgets = {
            'start_date': SelectDateWidget(years=range(now().year-10, now().year+10))
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        if start_date:
            # Calculate the end date as one year from the start date
            end_date = start_date + timedelta(days=365)
            cleaned_data['end_date'] = end_date
        return cleaned_data