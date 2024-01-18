from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    indebt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    invested = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def current_balance(self):
        return self.savings + self.invested - self.indebt

    def __str__(self):
        return self.user.username