from django.urls import path
from .views import (login_view, register_view, password_reset_view,
                    dashboard_view, logout_view, manage_settings_view,
                    update_user_view, delete_user)
from academy.views import (academy_articles_view)
from demo.views import (demo_dashboard_view, demo_income_view,
                    demo_expenditure_view, demo_manage_budgets)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('settings/', manage_settings_view, name='manage_settings'),
    path('settings/update/', update_user_view, name='update_user'),
    path('settings/delete/', delete_user, name='delete_user'),

]
