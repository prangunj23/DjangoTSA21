from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.
class Event(models.Model):
    username = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return f"{self.username}: {self.email} at {self.date}"