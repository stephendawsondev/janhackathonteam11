# Django
from django.urls import path, include

# Local
from .views import faq_view, contact_view, about_view, team_view, privacy_policy_view

urlpatterns = [
    path('faq/', faq_view, name='faq'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('team/', team_view, name='team'),
    path('privacy_policy/', privacy_policy_view, name='privacy_policy'),
]
