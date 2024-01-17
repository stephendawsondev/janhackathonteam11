from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard_view, faq_view, contact_view, about_view  # Import the new views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('', dashboard_view, name='dashboard'),  # URL pattern for the root path
    path('faq/', faq_view, name='faq'),  # Add FAQ URL pattern
    path('contact/', contact_view, name='contact'),  # Add Contact URL pattern
    path('about/', about_view, name='about'),  # Add About URL pattern
]

