from django import forms


from .models import Expense, TypicalExpense
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
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
            raise ValidationError('Enter an amount with up to two decimal places.')
        return amount