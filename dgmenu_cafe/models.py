import os
from random import randint

from django.db import models
from dgmenu_account.models import CustomUser as User


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"Cafe/{final_name}"


# Create your models here.

class Cafe(models.Model):
    Manager = models.ForeignKey(User, models.CASCADE, verbose_name='مدیر کافه')
    Cafe_Name = models.CharField(max_length=150, verbose_name='نام کافه', null=True, blank=True)
    Cafe_UserName = models.CharField(max_length=150, verbose_name='نام کاربری کافه ', null=True, blank=False)
    Cafe_Description = models.CharField(max_length=250, verbose_name='توضیح کافه', null=True, blank=True)
    Cafe_keywords = models.CharField(max_length=250, verbose_name='کلمات کیدی', null=True, blank=True)
    Cafe_Address = models.CharField(max_length=250, verbose_name='ادرس کافه', null=True, blank=True)
    Cafe_Tel1 = models.CharField(max_length=100, verbose_name='شماره تماس1', null=True, blank=True)
    Cafe_Tel2 = models.CharField(max_length=100, verbose_name='شماره تماس 2', null=True, blank=True)
    Cafe_Tel3 = models.CharField(max_length=100, verbose_name='شماره تماس 3', null=True, blank=True)
    Cafe_Email = models.CharField(max_length=200, verbose_name='ادرس ایمیل', null=True, blank=True)
    Cafe_Instagram = models.CharField(max_length=200, verbose_name='اینستاگرام', null=True, blank=True)
    Cafe_Opening_Hours = models.CharField(max_length=250, verbose_name='ساعت کاری', null=True, blank=True)
    Cafe_Header_Logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                                         verbose_name='Header_Logo')
    Cafe_favicon = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                                     verbose_name='favicon')
    Cafe_Apple_Touch_Icon152 = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                                                 verbose_name='Icon152')
    Cafe_Apple_Touch_Icon120 = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                                                 verbose_name='Icon120')
    Cafe_Apple_Touch_Icon76 = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                                                verbose_name='Icon76')
    Admin_Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال مدیرت')
    Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال کاربر')
    Submit_Time = models.DateTimeField()
    Last_Edit_Time = models.DateTimeField()
