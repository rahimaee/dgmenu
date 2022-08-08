from django.db import models
from dgmenu_account.models import CustomUser as User


# Create your models here.

class Cafe(models.Model):
    Manager = models.ForeignKey(User, models.CASCADE, verbose_name='مدیر کافه')
    Cafe_Name = models.CharField(max_length=150, verbose_name='', null=True, blank=True)
    Cafe_Description = models.CharField(max_length=250, verbose_name='', null=True, blank=True)
    Cafe_keywords = models.CharField(max_length=250, verbose_name='', null=True, blank=True)
    Cafe_Address = models.CharField(max_length=250, verbose_name='', null=True, blank=True)
    Cafe_Tel1 = models.CharField(max_length=100, verbose_name='', null=True, blank=True)
    Cafe_Tel2 = models.CharField(max_length=100, verbose_name='', null=True, blank=True)
    Cafe_Tel3 = models.CharField(max_length=100, verbose_name='', null=True, blank=True)
    Cafe_Email = models.CharField(max_length=200, verbose_name='', null=True, blank=True)
    Cafe_Instagram = models.CharField(max_length=200, verbose_name='', null=True, blank=True)
    Cafe_Opening_Hours = models.CharField(max_length=250, verbose_name='', null=True, blank=True)
    Cafe_Header_Logo = models.ImageField()
    Cafe_favicon = models.ImageField()
    Cafe_Apple_Touch_Icon152 = models.ImageField()
    Cafe_Apple_Touch_Icon120 = models.ImageField()
    Cafe_Apple_Touch_Icon76 = models.ImageField()
    Admin_Is_Active = models.BooleanField(default=False, verbose_name='')
    Is_Active = models.BooleanField(default=False, verbose_name='')
    Submit_Time = models.DateTimeField()
    Last_Edit_Time = models.DateTimeField()
