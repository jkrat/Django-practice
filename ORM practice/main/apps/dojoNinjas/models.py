from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    desc = models.TextField()
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    #one-to-many
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name = "ninjas")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
