from django.db import models


class ArticleAcademy(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=528)
    url = models.URLField(max_length=1024, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s expense on {self.date}"

    class Meta:
        ordering = ['title']
        verbose_name_plural = "ArticleAcademy"

    def __str__(self):
        return self.title
