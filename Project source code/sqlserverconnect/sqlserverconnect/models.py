from django.db import models

class sqlserverconn(models.Model):
    studentID=models.IntegerField()
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class question(models.Model):
    questionID=models.IntegerField()
    question=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)
    mark=models.IntegerField()


class teacher(models.Model):
    teacherID=models.IntegerField()
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class question_and_answer(models.Model):
    questionID=models.IntegerField()
    question=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)
    mark=models.IntegerField()