from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

class Scores(models.Model):
    name = models.CharField(max_length=10)
    score1 = models.CharField(max_length=10)
    score2 = models.CharField(max_length=10)
    score3 = models.CharField(max_length=10)
