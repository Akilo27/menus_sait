from django.db import models

class Blog(models.Model):
    username = models.CharField(max_length=12)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

