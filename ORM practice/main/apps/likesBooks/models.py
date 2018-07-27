from __future__ import unicode_literals
from django.db import models

# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     desc = models.TextField(255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     #One to Many
#     uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "uploaded_books")
#     #Many to Many
#     liked_users = models.ManyToManyField(User, related_name = "liked_books")

class User(models.Model):
    name = models.CharField(max_length=255)
        #Many to Many
    likers = models.ManyToManyField("self", related_name = "likees")



class Buser(models.Model):
    name = models.CharField(max_length=255)
        #Many to Many
    connector = models.ForeignKey("self", on_delete=models.CASCADE, related_name = "connectee")



class Person(models.Model):
    name = models.CharField(max_length=255)
    

class Connection(models.Model):
    name = models.CharField(max_length=255)
    #One to Many
    connector = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "connectee")
    #One to Many
    connectee = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = "connector")




