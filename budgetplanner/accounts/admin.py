from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'indebt',
        'savings',
        'invested',
    )

    list_filter = ('user', )
    search_fields = ['user', 'email',]

    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)