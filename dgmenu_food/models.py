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


# Create your models here.
class Food(models.Model):
    Image = models.ImageField(default='avatar.png', upload_to=upload_image_path, verbose_name='عکس اصلی غذا')
    Title = models.CharField(max_length=200, null=False, verbose_name='')
    Description_Short = models.CharField(max_length=250, verbose_name='')
    Description_Long = models.CharField(max_length=500, verbose_name='')
    Ingredients = models.CharField(max_length=250, verbose_name='')
    Calories = models.CharField(max_length=50, verbose_name='')
    Tag = models.CharField(max_length=250, verbose_name='')
    Allergy = models.CharField(max_length=250, verbose_name='')
    Price = models.CharField(max_length=100, verbose_name='')
    Discount = models.CharField(max_length=200, null=True, blank=True, verbose_name='')
