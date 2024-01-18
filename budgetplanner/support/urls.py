# Django Imports
from django.urls import path, include

from .views import faq_view, contact_view, about_view

urlpatterns = [
    path('faq/', faq_view, name='faq'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]
