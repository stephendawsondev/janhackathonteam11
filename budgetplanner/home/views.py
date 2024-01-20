from django.shortcuts import render
from accounts.utils import anonymous_required
from django.contrib import messages
from datetime import datetime
import random


def home(request):
    return render(request, 'home/index.html')
