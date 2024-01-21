from django.urls import path
from .views import academy_articles_view

urlpatterns = [
    path('academy/articles/', academy_articles_view, name='academy_articles'),
]
