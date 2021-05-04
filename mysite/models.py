from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100),
    author = models.CharField(max_length=50)

    @classmethod
    def create(cls, title, author):
        book = cls(title=title, author = author)
        return book

