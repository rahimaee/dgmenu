from django.db import models
from dgmenu_cafe.models import Cafe


# Create your models here.

class FoodCategory(models.Model):
    Cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, verbose_name='')
    NameFa = models.CharField(max_length=120, verbose_name='')
    NameEn = models.CharField(max_length=120, verbose_name='')
    IsActive = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    IsActiveAdmin = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    Parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    First = models.IntegerField()
