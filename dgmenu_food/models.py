import os
from random import randint

from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"comestible/{final_name}"


def upload_image_gallery_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"comestible/gallery/{final_name}"


# Create your models here.
class Food(models.Model):
    Image = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس اصلی غذا')
    Title = models.CharField(max_length=200, null=False, verbose_name='نام')
    Description_Short = models.CharField(max_length=250, verbose_name='توضیح کوتاه')
    Description_Long = models.CharField(max_length=500, verbose_name='توضیح زیاد')
    Ingredients = models.CharField(max_length=250, verbose_name='مواد تشکیل دهنده')
    Calories = models.CharField(max_length=50, verbose_name='کالری')
    Tag = models.CharField(max_length=250, verbose_name='برچسب ها')
    Allergy = models.CharField(max_length=250, verbose_name='الرژی')
    Price = models.CharField(max_length=100, verbose_name='قیمت')
    Discount = models.CharField(max_length=200, null=True, blank=True, verbose_name='قیمت باتخفیف')
    Admin_Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال مدیر')
    Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Submit_Time = models.DateTimeField()
    Last_Edit_Time = models.DateTimeField()


class Gallery(models.Model):
    Image = models.ImageField(upload_to=upload_image_gallery_path, null=True, blank=True, verbose_name='تصویر')
    Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="images")
    Admin_Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال مدیر')
    Is_Active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Submit_Time = models.DateTimeField()
    Last_Edit_Time = models.DateTimeField()
