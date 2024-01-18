from django.urls import path
from .views import login_view, register_view, password_reset_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
