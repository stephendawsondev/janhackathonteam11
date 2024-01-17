from django.shortcuts import render

def login_view(request):
    # Render the login.html template located under accounts/templates/
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')
# Create your views here.
def faq_view(request):
    return render(request, 'faq.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')