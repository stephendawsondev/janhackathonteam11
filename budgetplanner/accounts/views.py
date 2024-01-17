from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserProfile
from transactions.models import Budget

from django.urls import reverse
from django.contrib.auth import authenticate, login
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        # Get username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to the dashboard view
            return redirect(reverse('dashboard'))  
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # Render the login form template if not a POST request
        return render(request, 'login.html')



def dashboard_view(request):
    context = {}
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            context['user_profile'] = user_profile
            context['current_balance'] = user_profile.current_balance()
        except UserProfile.DoesNotExist:
            context['user_profile'] = None
    return render(request, 'dashboard.html', context)
# Create your views here.
def faq_view(request):
    return render(request, 'faq.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')