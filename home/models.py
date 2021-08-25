from django.db import models
# Create your models here.


class Problems(models.Model):
    statement = models.CharField(max_length=1000)
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=1000)
    difficulty = models.CharField(max_length=15)


class Solution(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=1000)
    submittedAt = models.DateTimeField('submitted at')


class testCases(models.Model):
    input = models.CharField(max_length=1000)
    output = models.CharField(max_length=1000)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
