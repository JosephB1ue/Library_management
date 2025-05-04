from django.db import models

class Book_table(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    contact = models.BigIntegerField()


# Create your models here.
