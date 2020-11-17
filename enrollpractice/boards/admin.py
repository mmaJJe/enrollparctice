from django.contrib import admin
from .models import EnrollNumber, EnrollRank, EnrollStartTime
# Register your models here.
admin.site.register(EnrollNumber)
admin.site.register(EnrollRank)
admin.site.register(EnrollStartTime)