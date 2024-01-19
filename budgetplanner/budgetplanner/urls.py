from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('', include('accounts.urls')),
    path('', include('transactions.urls')),
    path('', include('support.urls')),
]
