from django.db import models
from django.contrib.auth.models import User

class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)  # <-- add null=True
    subject = models.CharField(max_length=255, blank=True, null=True)
    bookshelves = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    text_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
