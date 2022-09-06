from django.db import models

class connectDatabaseToDjango(models.Model):
    StudentID=models.IntegerField()
    FullName=models.CharField(max_length=100)
    Age=models.IntegerField()