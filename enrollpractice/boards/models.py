from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EnrollStartTime(models.Model):
    startTime = models.DateTimeField()

class EnrollNumber(models.Model):
    number = models.CharField(max_length=4)
    enrollStartTime = models.ForeignKey(EnrollStartTime, on_delete=models.CASCADE, null=True, blank=True,)

class EnrollRank(models.Model):
    enrollNumber = models.ForeignKey(EnrollNumber, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    enrollStartTime = models.ForeignKey(EnrollStartTime, on_delete=models.CASCADE, null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)