# Django
from django.urls import path

# Local
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
