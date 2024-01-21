from django.urls import path
from .views import (login_view, register_view, password_reset_view,
                    dashboard_view, logout_view)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
