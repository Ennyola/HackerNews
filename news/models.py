from datetime import datetime
from django.db import models

# Create your models here.


class Item(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    by = models.CharField(max_length=500,  null=True)
    title = models.CharField(max_length=500,  null=True)
    time = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    type = models.CharField(max_length=500, default="story")
    url = models.CharField(max_length=500, null=True)
    descendants = models.IntegerField(null=True)
    score = models.IntegerField(null=True)
    kids = models.JSONField(null=True)
    deleted = models.BooleanField(null=True)
    dead = models.BooleanField(null=True)
    parent = models.IntegerField(null=True)
    text = models.TextField(null=True)
    parts = models.JSONField(null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
