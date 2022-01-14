from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.
DIFFICULTY = [
    ("NOVICE", "novice"), 
    ("INTERMEDIATE", "intermediate"), 
    ("ADVANCED", "advanced")

]
element = []
for x in range(len(DIFFICULTY)):
    element.append(DIFFICULTY[x][1])

class Event(models.Model):
    username = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    lichessusername = models.CharField(max_length=64)
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY, default="NOVICE")

    def __str__(self):
        return f"{self.username}: {self.email} at level {self.difficulty} with username {self.lichessusername}"