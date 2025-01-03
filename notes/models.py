from django.db import models

# Create your models here.

class Note(models.Model):
    header = models.CharField(max_length=32)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
