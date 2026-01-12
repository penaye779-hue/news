from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)           # Book title (up to 200 chars)
    author = models.CharField(max_length=100)          # Author name (up to 100 chars)
    publication_year = models.IntegerField()           # Year of publication

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
