from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.word

class SavedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    bookshelves = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    text_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.title}: {self.text}"

class ArticleWord(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    frequency = models.IntegerField(default=1)

    class Meta:
        unique_together = ("article", "word")

class UserWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    due_date = models.DateField()
    known = models.BooleanField(default=False)