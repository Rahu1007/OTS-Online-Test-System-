from django.db import models # type: ignore

#class Candidate(models.Model):
#    username = models.CharField(primary_key=True, max_length=20)
#    password = models.CharField(null=False, max_length=20)
#    name = models.CharField(null=False, max_length=20)
#    test_attempted = models.IntegerField()
#    points = models.FloatField()

class Candidate(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(null=False, max_length=20)
    name = models.CharField(null=False, max_length=20)
    test_attempted = models.IntegerField(default=0)
    points = models.FloatField(default=0.0)
    email = models.EmailField(null=True)  # Add a new field


class Question(models.Model):  # Fixed typo here
    qid = models.BigAutoField(primary_key=True, auto_created=True)
    que = models.TextField()
    a = models.CharField(max_length=225)
    b = models.CharField(max_length=225)
    c = models.CharField(max_length=225)
    d = models.CharField(max_length=225)
    ans = models.CharField(max_length=2)

class Result(models.Model):
    resultid = models.BigAutoField(primary_key=True, auto_created=True)
    username = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt = models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField()
    points = models.IntegerField()
