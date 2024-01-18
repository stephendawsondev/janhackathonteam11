from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    indebt = forms.DecimalField(max_digits=10, decimal_places=2)
    savings = forms.DecimalField(max_digits=10, decimal_places=2)
    invested = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                indebt=self.cleaned_data['indebt'],
                savings=self.cleaned_data['savings'],
                invested=self.cleaned_data['invested']
            )
        return user
