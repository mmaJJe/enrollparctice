from django.db import models

# Create your models here.
class EnrollStartTime(models.Model):
    startTime = models.DateTimeField()

class EnrollNumber(models.Model):
    number = models.CharField(max_length=4)
    enrollStartTime = models.ForeignKey(EnrollStartTime, on_delete=models.CASCADE)

class EnrollRank(models.Model):
    enrollNumber = models.ForeignKey(EnrollNumber, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    enrollStartTime = models.ForeignKey(EnrollStartTime, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
