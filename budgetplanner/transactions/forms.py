from django import forms
from datetime import date, timedelta
from .models import MonthlyBudget,WeeklyBudget,YearlyBudget
from .models import Expense, TypicalExpense, Income, TypicalIncome
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.forms.widgets import HiddenInput
from django.forms import SelectDateWidget
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
        self.fields['typical_expense'].queryset = TypicalExpense.objects.all()
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
        self.fields['typical_income'].queryset = TypicalIncome.objects.all()
        self.fields['typical_income'].empty_label = "Select a typical income"

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError("The amount cannot be negative.")
        return amount

class WeeklyBudgetForm(forms.ModelForm):
    class Meta:
        model = WeeklyBudget
        fields = ['amount', 'start_date', 'end_date']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'start_date': HiddenInput(),  # Hide since it will be set automatically
            'end_date': HiddenInput(),  # Hide since it will be set automatically
        }
        help_texts = {
            'amount': 'Enter the total amount you plan to spend for the week.',
        }
        error_messages = {
            'amount': {
                'invalid': 'Please enter a valid amount with two decimal places.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Automatically calculate and set start and end dates
        self.fields['start_date'].initial = calculate_start_date()
        self.fields['end_date'].initial = self.fields['start_date'].initial + timedelta(days=6)
        self.fields['start_date'].disabled = True
        self.fields['end_date'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['start_date'] = calculate_start_date()
        cleaned_data['end_date'] = cleaned_data['start_date'] + timedelta(days=6)
        return cleaned_data

class MonthlyBudgetForm(forms.ModelForm):
    class Meta:
        model = MonthlyBudget
        fields = ['amount', 'month']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'month': SelectDateWidget()
        }
        error_messages = {
            'amount': {
                'invalid': 'Please enter a valid amount with two decimal places.',
            },
        }

class YearlyBudgetForm(forms.ModelForm):

    class Meta:
        model = YearlyBudget
        fields = ['amount', 'year']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'year': SelectDateWidget(years=range(datetime.now().year-10, datetime.now().year+10))
        }
        error_messages = {
            'amount': {
                'invalid': 'Please enter a valid amount with two decimal places.',
            },
        }
