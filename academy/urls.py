# Django
from django.urls import path

# Locals
from .views import academy_articles_view

urlpatterns = [
    path('academy/articles/', academy_articles_view, name='academy_articles'),
]
