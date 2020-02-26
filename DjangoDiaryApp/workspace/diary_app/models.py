# coding: utf-8
from django.db import models
from datetime import date

class Diary(models.Model):
    date = models.DateField(default=date.today, primary_key=True)
    title = models.CharField(max_length=128)
    body = models.TextField()
    weather = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publishing = models.BooleanField(default=True)