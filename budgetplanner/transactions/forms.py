from django import forms
from .models import Expense

# Example list of typical expenses, you can replace it with a model if needed.
TYPICAL_EXPENSES_CHOICES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Rent', 'Rent'),
    ('Utilities', 'Utilities'),
    # Add more options as needed
]

class ExpenseForm(forms.ModelForm):
    amount = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        widget=forms.NumberInput(attrs={'step': '0.01'}),
        help_text='Enter the amount. Only two decimal places are allowed.'
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Select the date of the expense.'
    )
    description = forms.CharField(
        widget=forms.Textarea,
        help_text='Enter a description of the expense.'
    )
    is_recurring = forms.BooleanField(
        required=False, 
        help_text='Check this box if the expense is recurring.'
    )

    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date', 'is_recurring']