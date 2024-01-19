from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'indebt',
        'savings',
        'invested',
    )

    list_filter = ('user', )
    search_fields = ['user', 'indebt', 'savings', 'invested']

    ordering = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
