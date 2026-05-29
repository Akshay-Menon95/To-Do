from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE

# Create your models here.
class todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    date=models.DateField()