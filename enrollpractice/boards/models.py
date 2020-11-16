from django.db import models

# Create your models here.
class EnrollNumber(models.Model):
    number = models.CharField(max_length=4)
    enrollStartTime = models.ForeignKey(EnrollStartTime, on_delete=models.CASCADE)

class EnrollStartTime(models.Model):
    startTime = models.DateTimeField()

class EnrollRank(models.Model):
    enrollNumber = models.ForeignKey(EnrollNumber, on_delete=models.CASCADE)
    enrollStartTime = models.ForeignKey(EnrollStartTime, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)