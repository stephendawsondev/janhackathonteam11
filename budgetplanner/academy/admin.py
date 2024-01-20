from django.contrib import admin
from .models import ArticleAcademy


class ArticleAcademyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'url',
        'status',
        'created_on',
    )

    list_filter = ('status', 'created_on')
    search_fields = ['title', 'description', 'url',]

    ordering = ('-created_on',)


admin.site.register(ArticleAcademy, ArticleAcademyAdmin)
