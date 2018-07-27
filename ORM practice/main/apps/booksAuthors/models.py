from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #Many to Many
    books = models.ManyToManyField(Book, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)