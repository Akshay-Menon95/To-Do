from django.db import models

# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()