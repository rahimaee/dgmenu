from django.db import models


# Create your models here.

class CafeUser(models.Model):
    NameFamily = models.CharField(max_length=200, verbose_name='نام و نام خانوداگی')
    PhoneNumber = models.CharField(max_length=11, verbose_name='شماره موبایل')

