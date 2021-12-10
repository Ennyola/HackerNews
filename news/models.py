from datetime import datetime
from django.db import models

# Create your models here.


class News(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    by = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    descendants = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    kids = models.JSONField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    dead = models.BooleanField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    # @property
    # def time(self):
    #     return datetime.utcfromtimestamp(self._time).strftime('%Y-%m-%d %H:%M:%S')

    # @time.setter
    # def time(self, time):
    #     self._time = time

    def __str__(self):
        return self.title
