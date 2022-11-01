from django.db import models


# Create your models here.

class ViewOfPage(models.Model):
    User = models.CharField(max_length=250, blank=True)
    Time = models.DateTimeField()
    Page = models.CharField(max_length=250)
